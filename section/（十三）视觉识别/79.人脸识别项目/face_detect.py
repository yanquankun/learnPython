import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path

# 加载训练数据
recogizer = cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')

# 设置名字和标签
names = ["YQK", "UNKNOW"]  # 名字
idn = [1, 2]  # 标签

# 设置名字和标签的映射关系
id_to_name = {1: "YQK"}  # 只有已知的ID才有对应的名字


def draw_chinese_text(img, text, position, color=(0, 255, 0), font_size=24):
    """在OpenCV图片上绘制中文"""
    # OpenCV的BGR转为RGB
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    # 字体路径（可根据实际情况修改为本地支持中文的字体）
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"  # macOS 示例
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=color)
    # RGB转回BGR
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)


# 识别图片
def face_detect_demo(img):
    # 获取灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 调用人脸分类器
    haar_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_detector = cv2.CascadeClassifier(haar_path)

    # 读取人脸特征并返回人脸坐标
    face_detect = face_detector.detectMultiScale(gray, 1.1, 5, 0, (100, 100), (800, 800))

    for x, y, w, h in face_detect:
        # 标记人脸
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)

        # 识别人脸
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        print(f"预测ID: {ids}, 置信度: {confidence:.2f}")

        # 根据置信度和ID来判断身份
        if confidence < 50 and ids in id_to_name:  # 调整阈值到50
            # 识别为已知人员
            name = id_to_name[ids]
            color = (0, 255, 0)  # 绿色
            print(f"{name}来了")
        else:
            # 识别为陌生人
            name = "陌生人"
            color = (0, 0, 255)  # 红色
            print("陌生人")

        # 判断是否有中文
        if any('\u4e00' <= ch <= '\u9fff' for ch in name):
            img = draw_chinese_text(img, name, (x, y - 30), color, font_size=28)
        else:
            cv2.putText(img, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        # 显示置信度
        cv2.putText(img, f"Conf: {confidence:.1f}", (x, y + h + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2.imshow("Face Detection", img)


def enumerate_cameras(max_devices=5):
    print("正在枚举可用摄像头设备：")
    for i in range(max_devices):
        cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
        if cap.isOpened():
            print(f"摄像头设备 {i} 可用")
            cap.release()
        else:
            print(f"摄像头设备 {i} 不可用")


# 枚举摄像头（如需可注释掉）
# enumerate_cameras(5)

# 进行视频画面捕获
# 如果你是调用的macOS的摄像头，通常是0
# 如果你有多个摄像头，可能需要调整索引
# 比如你发现了经常会调起ios的摄像头，那么可以切换到1的索引
# cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)

while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        print('按下空格键退出')
        break

cv2.destroyAllWindows()
cap.release()
