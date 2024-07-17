import cv2
from matplotlib import pyplot as plt
import os
import numpy as np


# plt显示彩色图片
def plt_show0(img):
    # cv2与plt的图像通道不同：cv2为[b,g,r];plt为[r, g, b]
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])
    plt.imshow(img)
    plt.show()


# plt显示灰度图片
def plt_show(img):
    plt.imshow(img, cmap='gray')
    plt.show()


# 图像去噪灰度处理
def gray_guss(image):
    image = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_image

def mask_gray_guss(image):
    # 将图像转换为HSV颜色空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 定义颜色的HSV范围
    lower_blue = np.array([100, 80, 80])  # 蓝色范围
    upper_blue = np.array([120, 255, 255])
    lower_yellow = np.array([25, 100, 100])  # 黄色范围
    upper_yellow = np.array([35, 255, 255])
    lower_green = np.array([55, 100, 100])  # 绿色范围
    upper_green = np.array([75, 255, 255])
    # 创建颜色掩码
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    # 合并掩码
    mask_combined = mask_blue | mask_yellow | mask_green
    # 应用掩码到原始图像
    masked_image = cv2.bitwise_and(image, image, mask=mask_combined)
    # 转换为灰度图像
    gray_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
    return  gray_image


# 读取待检测图片
origin_image = cv2.imread(r"D:\shixun\sss\test\rotatedimage.jpg")
# 复制一张图片，在复制图上进行图像操作，保留原图
image = origin_image.copy()
# 图像去噪灰度处理
gray_image = mask_gray_guss(image)
# x方向上的边缘检测（增强边缘信息）
Sobel_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0)
absX = cv2.convertScaleAbs(Sobel_x)
image = absX



# 图像阈值化操作——获得二值化图
ret, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
# 显示灰度图像
plt_show(image)
# 形态学（从图像中提取对表达和描绘区域形状有意义的图像分量）——闭操作
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 10))
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernelX, iterations=1)
# 显示灰度图像
plt_show(image)



# 腐蚀（erode）和膨胀（dilate）
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 1))
kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
# x方向进行闭操作（抑制暗细节）
image = cv2.dilate(image, kernelX)
image = cv2.erode(image, kernelX)
# y方向的开操作
image = cv2.erode(image, kernelY)
image = cv2.dilate(image, kernelY)
# 中值滤波（去噪）
image = cv2.medianBlur(image, 21)
# 显示灰度图像
plt_show(image)
# 获得轮廓
contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for item in contours:
    # rect = cv2.boundingRect(item)
    # x = rect[0]
    # y = rect[1]
    # weight = rect[2]
    # height = rect[3]
    # # 根据轮廓的形状特点，确定车牌的轮廓位置并截取图像
    # if (weight > (height * 2)) and (weight < (height * 5)):
    #     image = origin_image[y:y + height, x:x + weight]
    #     plt_show0(image)
if contours:
    # 获取最大轮廓
    contour = max(contours, key=cv2.contourArea)

    # 获取最小外接矩形
    rect = cv2.minAreaRect(contour)

    # 获取四个顶点
    box = cv2.boxPoints(rect)
    # box = np.int0(box)  # 转换为整数

    # # 打印四个顶点坐标
    # for point in box:
    #     print(point)
    #
    # # 可视化结果
    # cv2.drawContours(gray_image, [box], -1, (255, 0, 0), 2)  # 绘制外接矩形
    # cv2.imshow('Detected Rectangle', gray_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    pts_src = box

    # 定义输出图像的大小，可以根据需要调整
    width = 440  # 输出图像宽度
    height = 140  # 输出图像高度

    # 定义目标图像的四个顶点坐标
    pts_dst = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype=np.float32)

    # 计算透视变换矩阵
    matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)

    # 进行透视变换
    result_image = cv2.warpPerspective(origin_image, matrix, (width, height))

    # 显示原始图像和透视变换后的结果
    cv2.imshow('Original Image', origin_image)
    cv2.imshow('Perspective Transform', result_image)
    cv2.waitKey(0)




