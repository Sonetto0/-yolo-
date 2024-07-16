# coding:utf-8
import os
import sys
import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout

from qfluentwidgets import ImageLabel, HorizontalFlipView, BodyLabel, TitleLabel, CaptionLabel, LargeTitleLabel, \
    StrongBodyLabel, PushButton, FluentIcon, ComboBox, PrimaryPushButton, MessageBox, TogglePushButton, CheckBox
from qfluentwidgets.multimedia import VideoWidget
from qframelesswindow import AcrylicWindow


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPixmap

from predict import predict, predict_i, predict_v, predict_i_s
from result_test import get_image_paths, predict_result, accuracy, predict_yan_result
from capture_show_test import CameraApp


class Window(AcrylicWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Main Window")
        self.titleBar.raise_()

        # customize acrylic effect
        # self.windowEffect.setAcrylicEffect(self.winId(), "106EBE99")

        # you can also enable mica effect on Win11
        # self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False, isAlt=False)

        self.bodyLabel = None
        # self.acc_bodyLabel = None
        self.l_bodyLabel = None
        self.folder_bodyLabel = None
        self.predict_file_path = None
        self.model_path = r"D:\shixun\sss\model\yan_v1.pt"
        self.camera_app = CameraApp()
        self.mode = False
        self.acc = 0.01
        # self.predictResult = []

        self.initUI()

    def initUI(self):

        titleLabel = LargeTitleLabel("2024实训项目")
        captionLabel = CaptionLabel("yolo识别验证码和车牌号的模型测试程序")

        pushButton = PushButton(FluentIcon.FOLDER, 'Folder')
        pushButton_iv = PushButton(FluentIcon.PHOTO, 'Picture Or Video')
        pushButton_ca = TogglePushButton(FluentIcon.CAMERA, 'Camera')
        pushButton.setFixedWidth(240)
        pushButton_iv.setFixedWidth(240)
        pushButton_ca.setFixedWidth(240)

        pushButton_ca.toggled.connect(lambda checked: self.openCamera(checked))

        self.checkBox = CheckBox("Perspective Transform")
        # Check the checkbox
        self.checkBox.setChecked(False)
        # Listen for checkbox state change signals
        self.checkBox.stateChanged.connect(lambda: print(self.checkBox.isChecked()))

        self.folder_bodyLabel = StrongBodyLabel()

        comboBox = ComboBox()
        # 添加选项
        items = ['验证码识别', '车牌号识别']
        comboBox.addItems(items)
        # 当前选项的索引改变信号
        comboBox.currentIndexChanged.connect(lambda index: self.set_model_path(index))
        # comboBox.currentIndexChanged.connect(lambda index: print(comboBox.currentText()))
        comboBox.setFixedWidth(300)



        start_button = PrimaryPushButton('启动')
        start_button.setFixedWidth(200)




        # self.bodyLabel = StrongBodyLabel()
        # self.acc_bodyLabel = StrongBodyLabel()
        self.l_bodyLabel = BodyLabel()


        # 添加图片
        # flipView.addImages([])
        # 监听当前页码改变信号


        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout(self)
        self.textLayout = QVBoxLayout(self)
        self.imgLayout = QHBoxLayout(self)

        self.vBoxLayout.addWidget(titleLabel)
        self.vBoxLayout.addSpacing(5)
        self.vBoxLayout.addWidget(captionLabel)
        # vBoxLayout.addWidget(image)
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addWidget(comboBox, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(pushButton, 0, Qt.AlignLeft)
        self.hBoxLayout.addWidget(pushButton_iv, 0, Qt.AlignLeft)
        self.hBoxLayout.addWidget(pushButton_ca, 0, Qt.AlignLeft)
        self.vBoxLayout.addSpacing(5)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addSpacing(5)
        self.vBoxLayout.addWidget(self.folder_bodyLabel)
        self.vBoxLayout.addSpacing(5)
        # vBoxLayout.addSpacing(20)
        self.vBoxLayout.addWidget(self.checkBox)
        self.vBoxLayout.addWidget(start_button, 0, Qt.AlignHCenter)
        # self.vBoxLayout.setSpacing(5)
        self.vBoxLayout.addWidget(self.l_bodyLabel)

        self.vBoxLayout.addLayout(self.imgLayout)


        pushButton.clicked.connect(self.msg)
        pushButton_iv.clicked.connect(self.msg_iv)
        start_button.clicked.connect(self.start)

    def updatePageIndex(self, index):
        # self.bodyLabel.setText(f"预测结果：{self.predictResult[index]}")
        if self.acc > 0.01:
            self.bodyLabel.setText(f" 预测结果：{self.predictResult[index]} \n 正确率为: {self.acc:.2%}")
        else:
            self.bodyLabel.setText(f" 预测结果：{self.predictResult[index]}")

    def msg(self, Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "D:/shixun/sss")  # 起始路径
        self.folder_bodyLabel.setText(m)
        self.predict_file_path = m
        print(self.predict_file_path)
    def msg_iv(self, Filepath):
        filter = "检测文件(*.jpg *.mp4)"
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(None, "选择文件", "D:/shixun/sss", filter)
        if files:
            self.folder_bodyLabel.setText(files[0])  # 这里假设只展示第一个文件的路径
            self.predict_file_path = files[0]


    def openCamera(self, checked):
        if self.mode:
            if checked:
                self.camera_app.open_c()
            else:
                self.camera_app.close_c()
        else:
            w = MessageBox("警告", "验证码识别模块目前只接受图片", self)
            w.yesButton.setText("确认")
            w.cancelButton.hide()
            w.buttonLayout.insertStretch(1)
            w.exec()



    def set_model_path(self, index):
        print(index)
        if index == 1:
            self.model_path = "D:\shixun\sss\model\che_v1.pt"
            self.mode = True
        elif index == 0:
            self.model_path = r"D:\shixun\sss\model\yan_v1.pt"
            self.mode =False


    def has_chinese(self, text):
        pattern = re.compile(r'[\u4e00-\u9fa5]')  # 中文字符的Unicode范围
        return bool(pattern.search(text))


    def start(self):
        self.delectLayout(self.imgLayout)
        if self.predict_file_path is None:
            w = MessageBox("警告", "未选择检测文件", self)
            w.yesButton.setText("确认")
            w.cancelButton.hide()
            w.buttonLayout.insertStretch(1)
            w.exec()

        elif self.model_path is None:
            w = MessageBox("警告", "未选择模型", self)
            w.yesButton.setText("确认")
            w.cancelButton.hide()
            w.buttonLayout.insertStretch(1)
            w.exec()

        else:
            # self.view.deleteLater()
            # self.bodyLabel.setText('')
            # self.acc_bodyLabel.setText('')
            if self.mode:
                if os.path.isdir(self.predict_file_path):
                    l = predict(self.model_path, self.predict_file_path)
                    speed = f"Preprocess time: {l['preprocess']:.2f} ms, Inference time: {l['inference']:.2f} ms, Postprocess time: {l['postprocess']:.2f} ms per image"
                    self.l_bodyLabel.setText(speed)

                    self.bodyLabel = StrongBodyLabel()
                    flipView = HorizontalFlipView()
                    flipView.currentIndexChanged.connect(lambda index: self.updatePageIndex(index))
                    flipView.setItemSize(QSize(640, 360))
                    flipView.setFixedSize(QSize(640, 360))
                    flipView.setBorderRadius(15)

                    flipView.addImages(get_image_paths(self.predict_file_path))
                    self.imgLayout.addWidget(flipView)

                    folder_path = r'D:\shixun\sss\Test'
                    self.predictResult = predict_result()
                    self.acc = accuracy(folder_path)
                    # print(type(acc))
                    # print(acc)

                    # self.textLayout.addWidget(self.bodyLabel)
                    if self.acc > 0.01:
                        # self.bodyLabel.setText(f" 预测结果：{self.predictResult[0]} \n 正确率为: {self.acc:.2%}")
                        if self.predictResult:
                            self.bodyLabel.setText(f" 预测结果：{self.predictResult[0]} \n 正确率为: {self.acc:.2%}")
                        else:
                            self.bodyLabel.setText("未检测到结果")
                    else:
                        # self.bodyLabel.setText(f" 预测结果：{self.predictResult[0]}")
                        if self.predictResult:
                            self.bodyLabel.setText(f"预测结果：{self.predictResult[0]}")
                        else:
                            self.bodyLabel.setText("未检测到结果")
                    self.imgLayout.addWidget(self.bodyLabel)
                        # self.textLayout.addWidget(self.acc_bodyLabel)

                    # self.imgLayout.addLayout(self.textLayout)
                    # self.imgLayout.update()
                    # self.vBoxLayout.addLayout(self.imgLayout)
                    # self.vBoxLayout.addWidget(self.view, 0, Qt.AlignHCenter)

                else:
                    _, file_extension = os.path.splitext(self.predict_file_path)
                    file_extension = file_extension.lower()
                    if file_extension == '.jpg':
                        if self.checkBox.isChecked() and self.has_chinese(self.predict_file_path):
                            w = MessageBox("提示", "使用perspective transform时不能包含中文路径", self)
                            w.yesButton.setText("确认")
                            w.cancelButton.hide()
                            w.buttonLayout.insertStretch(1)
                            w.exec()
                        else:
                            if self.checkBox.isChecked():
                                l = predict_i_s(self.model_path, self.predict_file_path)
                            else:
                                l = predict_i(self.model_path, self.predict_file_path)
                            speed = f"Preprocess time: {l['preprocess']:.2f} ms, Inference time: {l['inference']:.2f} ms, Postprocess time: {l['postprocess']:.2f} ms"
                            self.l_bodyLabel.setText(speed)
                            # self.flipView.addImages([r"D:\shixun\sss\runs\detect\predict\image0.jpg"])
                            # self.vBoxLayout.addWidget(self.flipView, 0, Qt.AlignHCenter)
                            # self.imgView.setPixmap(QPixmap(r"D:\shixun\sss\runs\detect\predict\image0.jpg"))
                            # imgView = QLabel(self)
                            # imgView.setFixedWidth(640)
                            # pixmap = QPixmap(r"D:\shixun\sss\runs\detect\predict\image0.jpg")
                            # imgView.setPixmap(pixmap.scaledToWidth(imgView.width()))
                            # self.view = imgView
                            # self.vBoxLayout.addWidget(self.view, 0, Qt.AlignLeft)
                            self.bodyLabel = StrongBodyLabel()
                            imgview = QLabel(self)
                            imgview.setFixedWidth(640)
                            pixmap = QPixmap(r"D:\shixun\sss\runs\detect\predict\image0.jpg")
                            imgview.setPixmap(pixmap.scaledToWidth(imgview.width()))
                            self.imgLayout.addWidget(imgview)
                            self.predictResult = predict_result()
                            # self.bodyLabel.setText(f" 预测结果：{self.predictResult[0]}")
                            if self.predictResult:
                                self.bodyLabel.setText(f"预测结果：{self.predictResult[0]}")
                            else:
                                self.bodyLabel.setText("未检测到结果")
                            self.imgLayout.addWidget(self.bodyLabel)
                            # self.imgLayout.update()



                    elif file_extension == '.mp4':
                        predict_v(self.model_path, self.predict_file_path)
                        # self.imgLayout.update()
                        # self.videoView = VideoWidget(self)
                        # video_url = QUrl.fromLocalFile(r"D:\Download\video0.mp4")
                        # # video_url = QUrl.fromLocalFile(r"D:\shixun\sss\runs\detect\predict\video0.mp4")
                        # video_content = QMediaContent(video_url)
                        # self.videoView.setVideo(video_content)
                        #
                        # self.vBoxLayout.addWidget(self.videoView)
                        # self.videoView.play()


                        # self.video_widget = QVideoWidget()
                        # # 创建媒体播放器
                        # self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
                        # self.media_player.setVideoOutput(self.video_widget)
                        # video_url = QUrl.fromLocalFile(r"D:\shixun\sss\runs\detect\predict\video0.mp4")  # 替换为你的视频文件路径
                        # video_content = QMediaContent(video_url)
                        # self.media_player.setMedia(video_content)
                        # self.vBoxLayout.addWidget(self.video_widget)
                        # self.media_player.play()
            else:
                _, file_extension = os.path.splitext(self.predict_file_path)
                file_extension = file_extension.lower()
                if file_extension == '.jpg':
                    print('yan')
                    l = predict_i(self.model_path, self.predict_file_path)
                    speed = f"Preprocess time: {l['preprocess']:.2f} ms, Inference time: {l['inference']:.2f} ms, Postprocess time: {l['postprocess']:.2f} ms"
                    self.l_bodyLabel.setText(speed)

                    self.bodyLabel = StrongBodyLabel()
                    imgview = QLabel(self)
                    imgview.setFixedWidth(640)
                    pixmap = QPixmap(r"D:\shixun\sss\runs\detect\predict\image0.jpg")
                    imgview.setPixmap(pixmap.scaledToWidth(imgview.width()))
                    self.imgLayout.addWidget(imgview)
                    self.predictResult = predict_yan_result()
                    # self.bodyLabel.setText(f" 预测结果：{self.predictResult[0]}")
                    if self.predictResult:
                        self.bodyLabel.setText(f"预测结果：{self.predictResult[0]}")
                    else:
                        self.bodyLabel.setText("未检测到结果")
                    self.imgLayout.addWidget(self.bodyLabel)


                else:
                    w = MessageBox("警告", "验证码识别模块目前只接受图片", self)
                    w.yesButton.setText("确认")
                    w.cancelButton.hide()
                    w.buttonLayout.insertStretch(1)
                    w.exec()





    def delectLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()









if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
