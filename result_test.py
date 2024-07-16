
# class_names = {
#     0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
#     10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j',
#     20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
#     30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: 'A', 37: 'B', 38: 'C', 39: 'DD',
#     40: 'E', 41: 'F', 42: 'G', 43: 'H', 44: 'I', 45: 'J', 46: 'K', 47: 'L', 48: 'M', 49: 'N',
#     50: 'O', 51: 'P', 52: 'Q', 53: 'R', 54: 'S', 55: 'T', 56: 'U', 57: 'V', 58: 'W', 59: 'X',
#     60: 'Y', 61: 'Z', 62: 'D'
# }


# import torch

import os


# def get_txt_paths(folder_path):
#     txt_extensions = ['txt']
#     txt_paths = []
#
#     # 遍历文件夹中的所有文件和子文件夹
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if any(file.lower().endswith(ext) for ext in txt_extensions):
#                 txt_paths.append(os.path.join(root, file))
#
#     return txt_paths

def get_txt_paths(folder_path):
    txt_extensions = ['txt']
    txt_paths = []

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in txt_extensions):
                file_path = os.path.join(root, file)
                txt_paths.append((file_path, os.path.getmtime(file_path)))

    # 按文件修改时间从最旧到最新排序
    txt_paths.sort(key=lambda x: x[1])

    # 只返回路径，不返回时间戳
    sorted_paths = [path for path, _ in txt_paths]

    return sorted_paths


class_names = {
    0: "plate", 1: "0", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8",
    10: "9", 11: "A", 12: "B", 13: "C", 14: "D", 15: "E", 16: "F", 17: "G", 18: "H", 19: "J",
    20: "K", 21: "L", 22: "M", 23: "N", 24: "P", 25: "Q", 26: "R", 27: "S", 28: "T", 29: "U",
    30: "V", 31: "W", 32: "X", 33: "Y", 34: "Z", 35: "澳", 36: "川", 37: "鄂", 38: "甘", 39: "赣",
    40: "港", 41: "贵", 42: "桂", 43: "黑", 44: "沪", 45: "吉", 46: "冀", 47: "津", 48: "晋", 49: "京",
    50: "警", 51: "辽", 52: "鲁", 53: "蒙", 54: "闽", 55: "宁", 56: "青", 57: "琼", 58: "陕", 59: "苏",
    60: "皖", 61: "湘", 62: "新", 63: "学", 64: "渝", 65: "豫", 66: "粤", 67: "云", 68: "浙", 69: "藏"
}


class_yan_names = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j',
    20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
    30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: 'A', 37: 'B', 38: 'C', 39: 'DD',
    40: 'E', 41: 'F', 42: 'G', 43: 'H', 44: 'I', 45: 'J', 46: 'K', 47: 'L', 48: 'M', 49: 'N',
    50: 'O', 51: 'P', 52: 'Q', 53: 'R', 54: 'S', 55: 'T', 56: 'U', 57: 'V', 58: 'W', 59: 'X',
    60: 'Y', 61: 'Z', 62: 'D'
}

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
# # Example tensor data (copied from your message)
# data = torch.tensor([
#     [ 83.00000,  63.00000, 101.00000,  98.00000,   0.94171,  22.00000],
#     [ 38.00000,  60.00000,  56.00000,  96.00000,   0.92729,  43.00000],
#     [141.00000,  64.00000, 160.00000,  99.00000,   0.90814,   3.00000],
#     [ 57.00000,  62.00000,  75.00000,  97.00000,   0.89937,  11.00000],
#     [121.00000,  63.00000, 140.00000,  99.00000,   0.88188,   8.00000],
#     [161.00000,  65.00000, 180.00000, 100.00000,   0.82705,   7.00000],
#     [102.00000,  63.00000, 121.00000,  97.00000,   0.82657,   7.00000],
#     [ 15.00000,  21.00000, 197.00000, 132.00000,   0.77590,   0.00000]
# ], device='cuda:0')
#
# # Call the function to print sorted classes as a concatenated string
# print_sorted_classes(data, class_names)


# 读取文件并处理
file_path = r"D:\shixun\sss\runs\detect\predict2\labels\image0.txt"  # 假设文件路径为 imagex.txt


def get_predict_results(file_path):
    # 读取文件内容


    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 解析每一行数据，提取类别和数据，并存入列表
    data = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 1:
            category = int(parts[0])
            if category != 0:  # 排除类别为0的数据
                data.append((category, line.strip()))

    data_sorted = sorted(data, key=lambda x: -float(x[1].split()[5]))

    # Keep up to 7 rows if more than 7 rows exist
    if len(data_sorted) > 7:
        data_sorted = data_sorted[:7]

    # 按照第二个数据（索引为1）从小到大排序
    data_sorted = sorted(data_sorted, key=lambda x: float(x[1].split()[1]))

    # 映射类别为字符串
    mapped_categories = [class_names[category] for category, _ in data_sorted]

    # 输出映射后的结果，拼接成一个字符串
    output_string = ' '.join(mapped_categories)

    output_string = output_string.replace(' ', '')

    # 打印输出结果
    # print(output_string)

    # print(file_path)

    return output_string


def get_yan_predict_results(file_path):
    # 读取文件内容


    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 解析每一行数据，提取类别和数据，并存入列表
    data = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 1:
            category = int(parts[0])
            if category != 0:  # 排除类别为0的数据
                data.append((category, line.strip()))

    data_sorted = sorted(data, key=lambda x: -float(x[1].split()[5]))

    # Keep up to 7 rows if more than 7 rows exist
    if len(data_sorted) > 7:
        data_sorted = data_sorted[:7]

    # 按照第二个数据（索引为1）从小到大排序
    data_sorted = sorted(data_sorted, key=lambda x: float(x[1].split()[1]))

    # 映射类别为字符串
    mapped_categories = [class_yan_names[category] for category, _ in data_sorted]

    # 输出映射后的结果，拼接成一个字符串
    output_string = ' '.join(mapped_categories)

    output_string = output_string.replace(' ', '')

    # 打印输出结果
    # print(output_string)

    # print(file_path)

    return output_string

def get_image_paths(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths

def predict_result():
    folder_path = r'D:\shixun\sss\runs\detect\predict\labels'  # 替换为实际的文件夹路径
    txt_paths = get_txt_paths(folder_path)

    print(txt_paths)
    predict_results = []

    for txt_path in txt_paths:
        predict_results.append(get_predict_results(txt_path))

    print(predict_results)
    # print(len(predict_results))
    return predict_results


def predict_yan_result():
    folder_path = r'D:\shixun\sss\runs\detect\predict\labels'  # 替换为实际的文件夹路径
    txt_paths = get_txt_paths(folder_path)

    print(txt_paths)
    predict_results = []

    for txt_path in txt_paths:
        predict_results.append(get_yan_predict_results(txt_path))

    print(predict_results)
    # print(len(predict_results))
    return predict_results



def accuracy(folder_path):
    predict_results = predict_result()

    image_paths = get_image_paths(folder_path)

    # 提取不带后缀的文件名部分
    file_names_no_extension = [os.path.splitext(os.path.basename(path))[0] for path in image_paths]

    # 打印输出所有找到的图片文件名（不带后缀）
    print(file_names_no_extension)

    if len(predict_results) == len(file_names_no_extension):
        # 计算总预测次数
        total_predictions = len(predict_results)

        # 计算预测正确的次数
        correct_predictions = sum(1 for pred, true in zip(predict_results, file_names_no_extension) if pred == true)

        # 计算正确率
        accuracy = correct_predictions / total_predictions

        # 打印结果
        print(f"正确率为: {accuracy:.2%}")
        return accuracy
    else:
        print("预测结果列表和正确结果列表长度不一致！")
        print(len(predict_results))
        print(len(file_names_no_extension))
        return 0

if __name__ == '__main__':
    r = predict_yan_result()
    # print(r)