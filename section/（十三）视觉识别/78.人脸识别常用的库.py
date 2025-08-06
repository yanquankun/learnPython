"""
@Desc: 本章节主要讲解人脸识别常用的库
@Author: Mint.Yan
@Date: 2025-08-218 13:59:43
"""

# 人脸识别的常用库有以下几种：
# 1. 基于特征向量方法：OpenCV
# 2. 基于 CNN 或 HOG 方法：Tensorflow、PyTorch

# 本节重点使用 OpenCV 库

# 下面，先配置 OpenCV 库的环境

# 安装 OpenCV 库
# 安装opencv的python库
# pip3.10 install opencv-python
# 安装Pillow库，它是Python Imaging Library的一个分支，提供了图像处理功能
# Pillow库是OpenCV的一个依赖库
# pip3.10 install Pillow
# 安装opencv的contrib库，它包含了人脸识别的相关模块
# pip3.10 install opencv-contrib-python

# 下面是opencv的一般使用流程：

# 1. 使用 OpenCV 读取和保存图片

# •  读取图片
# cv2.imread(图片路径和名称)
# •  显示图片
# cv2.imshow()
# •  保存图片
# cv2.imwrite()

# 2. 使用 OpenCV 标注图像

# 标注图像，用于调试时不断优化算法
# 一般采用矩形框对图像进行标注：
# cv.rectangle(图片，坐标，color=颜色，thickness=宽度)

# 下面我们以 /files/imgs/0d338744ebf81a4c87a3add4d52a6059252da61e.jpg 这张图举例

import cv2

# 读取图片，会将图片转换为 numpy 数组
pic = cv2.imread('../../files/imgs/0d338744ebf81a4c87a3add4d52a6059252da61e.jpg')

# 对图片进行矩形标注（当然，目前的标注区域是我们固定写入的，本节只为了基础演示，所以不做标注校验）
cv2.rectangle(pic, (70, 90), (170, 190), color=(0, 0, 255), thickness=2)

# 显示图片 此时会在一个新窗口中显示图片
# 注意：如果没有显示图片，可能是因为没有安装 Pillow 库
# 如果没有安装 Pillow 库，可以使用 pip3.10 install Pillow 命令安装
cv2.imshow('person', pic)
# 下面这两步是为了在窗口中显示图片，按下任意键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
