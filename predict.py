from ultralytics import YOLO

import os
from PIL import Image
import numpy as np

import torch


# class_names = {
#     0: "plate", 1: "0", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8",
#     10: "9", 11: "A", 12: "B", 13: "C", 14: "D", 15: "E", 16: "F", 17: "G", 18: "H", 19: "J",
#     20: "K", 21: "L", 22: "M", 23: "N", 24: "P", 25: "Q", 26: "R", 27: "S", 28: "T", 29: "U",
#     30: "V", 31: "W", 32: "X", 33: "Y", 34: "Z", 35: "澳", 36: "川", 37: "鄂", 38: "甘", 39: "赣",
#     40: "港", 41: "贵", 42: "桂", 43: "黑", 44: "沪", 45: "吉", 46: "冀", 47: "津", 48: "晋", 49: "京",
#     50: "警", 51: "辽", 52: "鲁", 53: "蒙", 54: "闽", 55: "宁", 56: "青", 57: "琼", 58: "陕", 59: "苏",
#     60: "皖", 61: "湘", 62: "新", 63: "学", 64: "渝", 65: "豫", 66: "粤", 67: "云", 68: "浙", 69: "藏"
# }
#
# def print_sorted_classes(data, class_names):
#     # Sort data by the first column (ascending order)
#     sorted_data = data[data[:, 0].argsort()]
#
#     # Initialize an empty string to store class names
#     sorted_classes_string = ""
#
#     # Concatenate class names in the sorted order, excluding class 0 ("plate")
#     for row in sorted_data:
#         cls = int(row[-1].item())  # Extract class label as integer
#         if cls != 0:
#             sorted_classes_string += class_names[cls]
#
#     # Print the concatenated string
#     print(sorted_classes_string)
#
#
# def print_mapped_classes(boxes):
#     # 定义映射关系
#     class_mapping = {
#         0: "plate",
#         1: "0", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9",
#         11: "A", 12: "B", 13: "C", 14: "D", 15: "E", 16: "F", 17: "G", 18: "H", 19: "J",
#         20: "K", 21: "L", 22: "M", 23: "N", 24: "P", 25: "Q", 26: "R", 27: "S", 28: "T",
#         29: "U", 30: "V", 31: "W", 32: "X", 33: "Y", 34: "Z",
#         35: "澳", 36: "川", 37: "鄂", 38: "甘", 39: "赣", 40: "港", 41: "贵", 42: "桂", 43: "黑",
#         44: "沪", 45: "吉", 46: "冀", 47: "津", 48: "晋", 49: "京", 50: "警", 51: "辽", 52: "鲁",
#         53: "蒙", 54: "闽", 55: "宁", 56: "青", 57: "琼", 58: "陕", 59: "苏", 60: "皖", 61: "湘",
#         62: "新", 63: "学", 64: "渝", 65: "豫", 66: "粤", 67: "云", 68: "浙", 69: "藏"
#     }
#
#     # 对boxes按第一列进行排序
#     sorted_boxes = boxes[boxes[:, 0].argsort()]
#
#     # 初始化结果字符串
#     result = []
#
#     # 遍历每一行数据
#     for box in sorted_boxes:
#         # 获取类别编号
#         class_index = int(box[-1].item())
#
#         # 排除标签为0（plate）的类别
#         if class_index == 0:
#             continue
#
#         # 获取类别名称
#         class_name = class_mapping[class_index]
#
#         # 添加到结果中
#         result.append(class_name)
#
#     # 拼接结果为一个字符串
#     result_str = ''.join(result)
#
#     # 打印结果
#     print(result_str)


# Load a model

def get_image_paths(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 可以根据需要添加其他图片格式的扩展名
    image_paths = []

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否为图片扩展名
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths


def open_images(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 可以根据需要添加其他图片格式的扩展名
    image_list = []

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否为图片扩展名
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_path = os.path.join(root, file)
                try:
                    img = Image.open(image_path)
                    image_list.append(img)
                except (IOError, OSError) as e:
                    print(f"Error opening {image_path}: {e}")

    return image_list

model = YOLO("yolov8n.pt")  # load an official model
model = YOLO(r"D:\shixun\sss\model\n100_train2.pt")  # load a custom model

# img = Image.open(r"D:\shixun\sss\Test\黑AM6726.jpg")
# img = np.array(img)
# img = Image.fromarray(img)

# Predict with the model
# results = model(img)  # predict on an image

model.predict(open_images(r"D:\shixun\sss\Test") , save=True, save_txt=True, imgsz=320, conf=0.5)

# for r in results:
#     print(r.boxes)  # print bbox predictions

    # confs = r.boxes.data[:, 4:6]  # Confidence and class ID of the detected objects
    # print(confs)
    # print(r.boxes.xyxy)
    # print(r.boxes.cls)

    # print(r.masks)  # print mask predictions
    # print(r.probs)  # print class probabilities
    # Call the function to print sorted classes as a concatenated string
    # boxes_np = r.boxes.cpu().numpy()

    # boxes = np.concatenate((r.boxes.xyxy, r.boxes.cls), axis=1)
    # r.boxes.cpu()
    # boxes = r.boxes.numpy()
    # print_sorted_classes(boxes, class_names)
    # print_mapped_classes(r.boxes)
