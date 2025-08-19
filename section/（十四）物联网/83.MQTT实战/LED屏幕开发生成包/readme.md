### 本文件是用来生成LED屏幕渲染程序的

```python
python3 oled_preview_and_export.py
```

它会在当前目录生成：
 
• oled_preview.png（128×64 的预览图）
• oled_preview@3x.png（放大预览）
• oled_layout.py（板端渲染器，等会儿一并拷到 ESP32）

你想改界面布局，就在 draw_ui() 里改，再运行脚本生成新的预览和渲染器

draw_ui在 oled_preview_and_export.py 里定义的
它的作用是：
1. 用 Pillow 在电脑上画出一个 128×64 模拟 OLED
2. 你可以在里面改布局、文字、图形，然后在 Mac 上跑出一张预览图
3. 运行脚本时，它会同时把界面“翻译”为板子能用的 oled_layout.py 渲染器