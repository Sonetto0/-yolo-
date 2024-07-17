import cv2
from ultralytics import YOLO
from cv2 import getTickCount, getTickFrequency


model_path = r"D:\shixun\sss\model\che_v1.pt"
model = YOLO(model_path)


class CameraApp:
    # def __init__(self):
    # self.cap = cv2.VideoCapture(0)



    def open_c(self):
        self.cap = cv2.VideoCapture(0)

        while self.cap.isOpened():
            # loop_start = getTickCount()
            success, frame = self.cap.read()  # 读取摄像头的一帧图像
            if success:
                model.predict(source=frame, show=True)  # 对当前帧进行目标检测并显示结果

    def close_c(self):
        self.cap.release()  # 释放摄像头资源
        cv2.destroyAllWindows()  # 关闭OpenCV窗口