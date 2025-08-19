# oled_preview_and_export.py
# Usage on Mac:
#   python3 oled_preview_and_export.py
# Requires: Pillow (pip install pillow)
#
# This script:
#  - Draws a 128x64 mock UI (title + temp/humi + bar)
#  - Saves a preview PNG to ./oled_preview.png
#  - Writes a MicroPython renderer to ./oled_layout.py (no external font needed)
#  - Can export a Chinese bitmap font and generate a renderer supporting Chinese + ellipsis
#
# You can edit the draw_ui() function below to change your layout.

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 128, 64  # SSD1306 common resolution
SP = 10  # fixed spacing between label and value

# ---- Chinese font candidates & loader (for preview) ----
CN_FONT_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Songti.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
]

def _get_cn_font(size):
    from PIL import ImageFont
    for p in CN_FONT_CANDIDATES:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


# ---- Preview helpers: text measuring & ellipsis for Pillow ----
def _text_width(draw, text, font):
    try:
        # Pillow >= 8.0
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0]
    except Exception:
        try:
            w, _ = draw.textsize(text, font=font)
            return w
        except Exception:
            return 0

def draw_text_with_ellipsis(draw, x, y, text, max_w, font, fill=1):
    """Draw text truncated with an ellipsis if it exceeds max_w pixels."""
    if text is None:
        return
    text = str(text)
    if _text_width(draw, text, font) <= max_w:
        draw.text((x, y), text, fill=fill, font=font)
        return
    # Try progressively shorter strings, then append ellipsis
    ell = "…"
    # If ellipsis itself wider than max_w, skip drawing
    if _text_width(draw, ell, font) > max_w:
        return
    lo, hi = 0, len(text)
    # binary search the longest prefix that fits with ellipsis
    while lo < hi:
        mid = (lo + hi + 1) // 2
        candidate = text[:mid] + ell
        if _text_width(draw, candidate, font) <= max_w:
            lo = mid
        else:
            hi = mid - 1
    draw.text((x, y), text[:lo] + ell, fill=fill, font=font)

# ---- Right-align helper for preview ----
def text_right_align(draw, y, text, font, right_margin_x):
    w = _text_width(draw, text, font)
    x = max(0, right_margin_x - w)
    draw.text((x, y), text, fill=255, font=font)


def collect_cn_chars_for_export():
    base = "wifi温度湿度°%/ ：:0123456789"
    return set(base)


# ---- Preview-side bitmap text (use same idea as device) ----
# We render on a 1-bit canvas for crisp pixels.

def _load_cn_font_data():
    try:
        import importlib
        font_cn = importlib.import_module('font_cn')
        return getattr(font_cn, 'FONT', {})
    except Exception:
        return {}

PREVIEW_CN_FONT = None  # lazy loaded


def _char_w_preview(draw, ch, ascii_font):
    # Chinese width from font_cn, ASCII width from bitmap font metrics
    global PREVIEW_CN_FONT
    if PREVIEW_CN_FONT is None:
        PREVIEW_CN_FONT = _load_cn_font_data()
    if ch in PREVIEW_CN_FONT or ch.encode('unicode_escape').decode('ascii') in PREVIEW_CN_FONT:
        g = PREVIEW_CN_FONT.get(ch) or PREVIEW_CN_FONT.get(ch.encode('unicode_escape').decode('ascii'))
        return g['w'] if g else 12
    # ASCII width measured from the font itself (bitmap, crisp)
    try:
        return draw.textlength(ch, font=ascii_font)
    except Exception:
        w = _text_width(draw, ch, ascii_font)
        return w if w else 8


def draw_text_mixed_preview(draw, x, y, text, max_w=None, ellipsis=True):
    """Draw mixed ASCII + Chinese using 1-bit crisp rendering.
    ASCII uses PIL's bitmap default font; Chinese uses font_cn bitmaps.
    """
    global PREVIEW_CN_FONT
    if PREVIEW_CN_FONT is None:
        PREVIEW_CN_FONT = _load_cn_font_data()
    ascii_font = ImageFont.load_default()
    text = str(text or '')

    # measure & ellipsis
    used = 0
    out = []
    for ch in text:
        cw = _char_w_preview(draw, ch, ascii_font)
        if max_w is not None and used + cw > max_w:
            # add ellipsis if it fits
            ell = '…'
            ell_w = _char_w_preview(draw, ell, ascii_font)
            if ellipsis and used + ell_w <= (max_w or 9999):
                out.append(ell)
            break
        out.append(ch)
        used += cw

    cx = x
    for ch in out:
        # Chinese from bitmap
        g = PREVIEW_CN_FONT.get(ch) or PREVIEW_CN_FONT.get(ch.encode('unicode_escape').decode('ascii'))
        if g:
            # draw bitmap pixels
            data = g['data']; w = g['w']; h = g['h']
            byte_idx = 0
            for yy in range(h):
                bits_left = 0; cur = 0
                for xx in range(w):
                    if bits_left == 0:
                        cur = data[byte_idx]; byte_idx += 1; bits_left = 8
                    bit = (cur & 0x80) != 0
                    cur = (cur << 1) & 0xFF; bits_left -= 1
                    if bit:
                        draw.point((cx + xx, y + yy), fill=1)
            cx += w
        else:
            # ASCII via bitmap font
            draw.text((cx, y), ch, font=ascii_font, fill=1)
            cw = _char_w_preview(draw, ch, ascii_font)
            cx += cw


def draw_ui(temp_c=23.4, humi=48.0, now_str="2025-08-19 20:15:00", wifi_on=True):
    # 1-bit canvas for crisp preview aligned with OLED
    img = Image.new("1", (W, H), 0)
    d = ImageDraw.Draw(img)

    # LINE 1: if wifi_on, show "wifi" + fixed spacing + datetime (YYYY-MM-DD HH:mm), else just datetime
    # Normalize without datetime/strptime (MicroPython-safe)
    s = str(now_str or "")
    if len(s) >= 16:
        dt_display = s[:16]  # take YYYY-MM-DD HH:mm
    else:
        try:
            import time
            t = time.localtime()
            dt_display = "%04d-%02d-%02d %02d:%02d" % (t[0], t[1], t[2], t[3], t[4])
        except Exception:
            dt_display = s

    if wifi_on:
        label = "wifi"
        ascii_font = ImageFont.load_default()
        label_w = sum(_char_w_preview(d, ch, ascii_font) for ch in label)
        draw_text_mixed_preview(d, 0, 2, label, max_w=W)
        draw_text_mixed_preview(d, label_w + SP, 2, dt_display, max_w=W)
    else:
        draw_text_mixed_preview(d, 0, 2, dt_display, max_w=W)

    # LINE 2: "温度：" + fixed spacing + value °C
    label_temp = "温度："
    ascii_font = ImageFont.load_default()
    label_temp_w = sum(_char_w_preview(d, ch, ascii_font) for ch in label_temp)
    draw_text_mixed_preview(d, 0, 24, label_temp, max_w=W)
    temp_text = "{:.1f}°C".format(temp_c)
    draw_text_mixed_preview(d, label_temp_w + SP, 24, temp_text, max_w=W)

    # LINE 3: "湿度：" + fixed spacing + value %
    label_humi = "湿度："
    label_humi_w = sum(_char_w_preview(d, ch, ascii_font) for ch in label_humi)
    draw_text_mixed_preview(d, 0, 42, label_humi, max_w=W)
    humi_text = "{:.1f}%".format(humi)
    draw_text_mixed_preview(d, label_humi_w + SP, 42, humi_text, max_w=W)

    # 边界像素（调试）
    d.point((W - 1, H - 1), fill=1)
    return img


def save_preview(img: Image.Image, out_path="oled_preview.png"):
    img1 = img.convert("1")  # hard-threshold to 1-bit to match OLED
    img1.save(out_path)
    print(f"[OK] Preview saved to {out_path}")
    try:
        img1.resize((W * 3, H * 3), resample=Image.NEAREST).save("oled_preview@3x.png")
        print("[OK] Also saved retina preview to oled_preview@3x.png")
    except Exception as e:
        print("[WARN] Could not save retina preview:", e)


# ---- Export Chinese bitmap font (to font_cn.py for MicroPython) ----
def export_cn_font(chars, out_path="font_cn.py", font_candidates=None, size=12):
    from PIL import Image, ImageDraw, ImageFont
    from pathlib import Path

    if isinstance(chars, str):
        chars = set(chars)

    if font_candidates is None:
        font_candidates = [
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/STHeiti Light.ttc",
            "/System/Library/Fonts/STHeiti Medium.ttc",
            "/System/Library/Fonts/Songti.ttc",
        ]

    font = None
    for fp in font_candidates:
        try:
            font = ImageFont.truetype(fp, size)
            break
        except Exception:
            continue
    if font is None:
        font = ImageFont.load_default()

    # Always include ellipsis
    chars = set(chars) | {"…"}

    glyphs = {}
    for ch in chars:
        canvas = Image.new("1", (size*2, size*2), 0)
        d = ImageDraw.Draw(canvas)
        d.text((0, 0), ch, fill=1, font=font)
        bbox = canvas.getbbox()
        if not bbox:
            continue
        x0, y0, x1, y1 = bbox
        w, h = x1 - x0, y1 - y0
        glyph = canvas.crop(bbox)

        rows = []
        for yy in range(h):
            byte = 0
            bits = 0
            line_bytes = []
            for xx in range(w):
                bit = 1 if glyph.getpixel((xx, yy)) else 0
                byte = (byte << 1) | bit
                bits += 1
                if bits == 8:
                    line_bytes.append(byte)
                    byte, bits = 0, 0
            if bits > 0:
                byte = byte << (8 - bits)
                line_bytes.append(byte)
            rows.extend(line_bytes)
        glyphs[ch] = {"w": w, "h": h, "data": rows}

    lines = []
    lines.append("# Auto-generated Chinese bitmap font")
    lines.append("FONT = {")
    for ch, g in glyphs.items():
        esc = ch.encode("unicode_escape").decode("ascii")
        lines.append(f"    '{esc}': {{'w': {g['w']}, 'h': {g['h']}, 'data': {g['data']}}},")
    lines.append("}")
    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Wrote Chinese font with {len(glyphs)} glyphs to {out_path}")


def write_renderer_py(out_path="oled_layout.py"):
    code = r"""# Auto-generated by oled_preview_and_export.py
# Layout:
#  L1: if wifi_on: "wifi" + fixed spacing + datetime string (YYYY-MM-DD HH:mm)
#      else: datetime string only
#  L2: "温度：" + fixed spacing + xx.x°C
#  L3: "湿度：" + fixed spacing + yy.y%

try:
    import font_cn
    CN_FONT = font_cn.FONT
except Exception:
    CN_FONT = {}

W = 128
H = 64
SP = 10

def _clip(v, lo, hi):
    return max(lo, min(hi, v))

def _char_width(ch):
    o = ord(ch)
    if 32 <= o <= 126:
        return 8
    g = CN_FONT.get(ch) or CN_FONT.get(ch.encode("unicode_escape").decode("ascii"))
    if g:
        return g['w']
    return 12

def _text_width(text):
    w = 0
    for ch in str(text or ""):
        w += _char_width(ch)
    return w

def _blit_bitmap(oled, x, y, w, h, data_bytes):
    byte_idx = 0
    for yy in range(h):
        bits_left = 0
        cur = 0
        for xx in range(w):
            if bits_left == 0:
                cur = data_bytes[byte_idx]
                byte_idx += 1
                bits_left = 8
            bit = (cur & 0x80) != 0
            cur = (cur << 1) & 0xFF
            bits_left -= 1
            if 0 <= x+xx < oled.width and 0 <= y+yy < oled.height:
                if bit:
                    oled.pixel(x+xx, y+yy, 1)

def _draw_glyph(oled, ch, x, y):
    o = ord(ch)
    if 32 <= o <= 126:
        yy = y if oled.height < 8 else _clip(y, 0, oled.height - 8)
        oled.text(ch, x, yy, 1)
        return x + 8
    g = CN_FONT.get(ch) or CN_FONT.get(ch.encode("unicode_escape").decode("ascii"))
    if g:
        _blit_bitmap(oled, x, y, g['w'], g['h'], g['data'])
        return x + g['w']
    return x + 12

def _draw_text(oled, text, x, y, max_w=None, ellipsis=True):
    text = str(text or "")
    used = 0
    out = []
    for ch in text:
        w = _char_width(ch)
        if max_w is not None and used + w > max_w:
            if ellipsis and used + _char_width('…') <= (max_w or 9999):
                out.append('…')
            break
        out.append(ch)
        used += w
    cx = x
    for ch in out:
        cx = _draw_glyph(oled, ch, cx, y)

def _normalize_dt(s):
    # Return YYYY-MM-DD HH:mm without using datetime/strptime (MicroPython-safe)
    s = str(s or "")
    if len(s) >= 16:
        return s[:16]
    try:
        from time import localtime
        t = localtime()
        return "%04d-%02d-%02d %02d:%02d" % (t[0], t[1], t[2], t[3], t[4])
    except Exception:
        return s

def render(oled, temp_c, humi, now_str, wifi_on):
    W = oled.width
    H = oled.height
    oled.fill(0)

    # Prepare datetime string in format YYYY-MM-DD HH:mm
    dt_display = _normalize_dt(now_str)

    # L1: if wifi_on, prefix "wifi" + fixed spacing + datetime, else datetime only
    if wifi_on:
        label = "wifi"
        label_w = _text_width(label)
        _draw_text(oled, label, 0, 2)
        _draw_text(oled, dt_display, label_w + SP, 2, max_w=W, ellipsis=True)
    else:
        _draw_text(oled, dt_display, 0, 2, max_w=W, ellipsis=True)

    # L2: "温度：" + fixed spacing + xx.x°C
    label_temp = "温度："
    label_temp_w = _text_width(label_temp)
    try:
        t_str = '{:.1f}'.format(temp_c)
    except Exception:
        t_str = 'NaN'
    temp_line = t_str + "°C"
    _draw_text(oled, label_temp, 0, 24)
    _draw_text(oled, temp_line, label_temp_w + SP, 24, max_w=W)

    # L3: "湿度：" + fixed spacing + yy.y%
    label_humi = "湿度："
    label_humi_w = _text_width(label_humi)
    try:
        h_str = '{:.1f}'.format(humi)
    except Exception:
        h_str = 'NaN'
    humi_line = h_str + "%"
    _draw_text(oled, label_humi, 0, 42)
    _draw_text(oled, humi_line, label_humi_w + SP, 42, max_w=W)

    oled.pixel(W-1, H-1, 1)
    oled.show()
"""
    Path(out_path).write_text(code, encoding="utf-8")
    print(f"[OK] Wrote MicroPython renderer to {out_path}")


if __name__ == "__main__":
    cn_chars = collect_cn_chars_for_export()
    export_cn_font(cn_chars, out_path="font_cn.py", size=12)

    img = draw_ui(23.4, 56.7, now_str="2025-08-19 20:15:00", wifi_on=True)
    save_preview(img)

    write_renderer_py()
    print("[DONE] Preview + font_cn.py + oled_layout.py are ready.")
