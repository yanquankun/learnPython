本单元将直接写一个简单的人脸识别项目，使用 OpenCV 和 Python 实现

将通过如下几个部分来完成：

1. 人脸捕获：

要想识别特定的人脸，需要对 OpenCV 的模型进行训练 
训练数据一般是从摄像头采集的截图，也可以是事先准备好的图片 

• 采集摄像头数据函数：cv.VideoCapture(0)

*cv.VideoCapture([VideoPath]) 除了捕获摄像头，还可以读取 MP4 格式的文件，通过读取视频可以反复优化 OpenCV 的模型*

• 从摄像头截图并保存文件函数：cv.imencode().tofile()


```python
# 本程序为人脸捕获程序
# 图片会保存到当前目录下的 imgData 文件夹中
# 后续我自己的照片和训练的识别模型数据会删除，各位可自己重新运行程序进行获取！！！
python3.10 face_cap.py
```

2. 人脸特征识别

`读取目录下全部训练文件`

训练人脸模型的图片，一般会存入到一个文件夹中，往往需要你遍历该目录，将所有文件的路径以字符串格式存放到一个列表中 

• 显示目录下所有文件：os.listdir() 
• 连接目录和文件：os.path.join()

`加载分类模型`

- 调用分类器  

cv.CascadeClassifier() 

- 人脸分类器 

```bash
# 该模型的位置在我们安装 OpenCV 的目录下
# 本项目位置在：
[你的项目位置]/venv/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml
```

`提取人脸特征值`

图片被转换为数组之后，通过特征提取函数将人脸特征值提取出来 
人脸特征提取函数：face_detect.detectMultiScale(图片数组) 

```python
# 本程序为人脸特征识别程序
python3.10 face_train.py
```