import cv2 as cv

cap = cv.VideoCapture(0)  # 0表示使用默认摄像头
num = 1  # 用于计数，保存图片的编号
face_name = 'Yqk'  # 人脸识别的名称
# id 必须为int类型，否则后面训练的时候会报错，OpenCV 的人脸识别器要求的是 整型（int32）的一维数组，不能是字符串类型
face_id = 1  # 人脸识别的ID

while (cap.isOpened()):
    # 捕获摄像头图片
    # ret_flag 表示是否成功捕获图片
    # vshow表示捕获的图片
    ret_flag, vshow = cap.read()
    # 显示捕获的图片
    cv.imshow('capture_yqk', vshow)
    # 图像刷新的频率
    k = cv.waitKey(1) & 0xFF
    # 设置按键保存图片
    if k == ord('s'):
        # 保存图片
        # cv.imencode()函数将图像编码为指定格式
        #   cv.imencode()返回一个元组，第一个元素是成功标志，第二个元素是编码后的图像
        # 这里使用.jpg格式保存图片
        # tofile()函数将编码后的图像保存到指定路径
        cv.imencode(".jpg", vshow)[1].tofile(f"./imgdata/{str(face_id)}_{face_name}_{str(num)}.jpg")
        print(f'保存图片：{face_name}_{face_id}_{num}.jpg')
        num += 1
    # 设置按键退出
    elif k == ord('q'):
        print('退出摄像头')
        break

# 关闭摄像头
cap.release()
# 销毁所有窗口
cv.destroyAllWindows()

# 可以看到imgdata中出现了很多我们自己的图片
