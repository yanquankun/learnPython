import cv2 as cv
from PIL import Image
import numpy as np
from pathlib import Path


# 注意：
# 确保只安装了 opencv-contrib-python，卸载其他版本 opencv-python
# opencv-python 和 opencv-contrib-python 不能同时安装，会导致模块冲突

# 如果你在运行本程序时，提示如下报错，那就是因为上面这个原因导致的
# recognizer = cv.face.LBPHFaceRecognizer_create()
# AttributeError: module 'cv2.face' has no attribute 'LBPHFaceRecognizer_create'


def getImageAndLabel(path):
    facesSamples = []
    ids = []

    # 调用人脸分类器（注意自己文件保存的路径，英文名）
    haar_path = cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_detect = cv.CascadeClassifier(haar_path)

    if face_detect.empty():
        print("错误：无法加载人脸分类器")
        return [], []

    # 循环读取照片人脸数据
    # 忽略.gitignore文件
    for imagePath in Path(path).rglob("*.jpg"):
        # 用灰度的方式打开照片
        PIL_img = Image.open(imagePath).convert('L')
        # 将照片转换为计算机能识别的数组OpenCV（BGR--0-255）
        img_numpy = np.array(PIL_img, 'uint8')
        # 提取图像中人脸的特征值
        faces = face_detect.detectMultiScale(img_numpy)
        # 将文件名按“.”进行分割
        id = int(imagePath.stem.split("_")[0])
        # 防止无人脸图像
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])

    return facesSamples, ids


faces, ids = getImageAndLabel('imgdata')

# 调用LBPH算法对人脸数据进行处理
if len(faces) == 0:
    print("错误：没有找到有效的人脸数据")
else:
    # 调用LBPH算法对人脸数据进行处理
    recognizer = cv.face.LBPHFaceRecognizer_create()

    # 训练数据
    recognizer.train(faces, np.array(ids))

    # 保存训练好的模型
    recognizer.write('./trainer/trainer.yml')
