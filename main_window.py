# coding:utf-8
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout

from qfluentwidgets import ImageLabel, HorizontalFlipView, BodyLabel, TitleLabel, CaptionLabel, LargeTitleLabel, \
    StrongBodyLabel
from qframelesswindow import AcrylicWindow


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap




class Window(AcrylicWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Acrylic Window")
        self.titleBar.raise_()

        # customize acrylic effect
        # self.windowEffect.setAcrylicEffect(self.winId(), "106EBE99")

        # you can also enable mica effect on Win11
        # self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False, isAlt=False)

        self.initUI()

    def initUI(self):

        titleLabel = LargeTitleLabel("智能识别")
        captionLabel = CaptionLabel("基于yolo识别验证码车牌号的系统")

        bodyLabel = StrongBodyLabel("当前页面：")

        flipView = HorizontalFlipView()
        # 添加图片
        flipView.addImages([r"D:\shixun\sss\Test\黑AM6726.jpg", r"D:\shixun\sss\Test\浙C51705.jpg"])
        # 监听当前页码改变信号
        flipView.currentIndexChanged.connect(lambda index: updatePageIndex(index))

        flipView.setItemSize(QSize(640, 360))
        flipView.setFixedSize(QSize(640, 360))
        flipView.setBorderRadius(15)

        vBoxLayout = QVBoxLayout(self)

        vBoxLayout.addWidget(titleLabel)
        vBoxLayout.addWidget(captionLabel)
        # vBoxLayout.addWidget(image)
        vBoxLayout.addSpacing(20)
        vBoxLayout.addWidget(flipView)
        vBoxLayout.addSpacing(20)
        vBoxLayout.addWidget(bodyLabel)

        def updatePageIndex(index):
            bodyLabel.setText(f"当前页面：{index}")


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
