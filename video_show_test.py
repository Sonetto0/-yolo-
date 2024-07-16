import sys
from pathlib import Path

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from qfluentwidgets import setTheme, Theme
from qfluentwidgets.multimedia import SimpleMediaPlayBar, StandardMediaPlayBar, VideoWidget

class Demo2(QWidget):

    def __init__(self):
        super().__init__()
        self.vBoxLayout = QVBoxLayout(self)
        self.videoWidget = VideoWidget(self)

        video_url = QUrl.fromLocalFile("D:\shixun\sss\runs\detect\predict\video0.mp4")
        # video_url = QUrl.fromLocalFile(r"D:\Download\video0.mp4")
        video_content = QMediaContent(video_url)
        # self.videoWidget.setMedia(video_content)

        self.videoWidget.setVideo(video_content)
        self.videoWidget.play()

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.videoWidget)
        self.resize(800, 450)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication([])
    # demo1 = Demo1()
    # demo1.show()
    demo2 = Demo2()
    demo2.show()
    sys.exit(app.exec())

