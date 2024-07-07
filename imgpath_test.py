# import os
#
# def get_image_paths(folder_path):
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 可以根据需要添加其他图片格式的扩展名
#     image_paths = []
#
#     # 遍历文件夹中的所有文件和子文件夹
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             # 检查文件扩展名是否为图片扩展名
#             if any(file.lower().endswith(ext) for ext in image_extensions):
#                 image_paths.append(os.path.join(root, file))
#
#     return image_paths
#
# # 示例用法
# folder_path = 'D:\shixun\sss\Test'  # 替换为实际的文件夹路径
# image_paths = get_image_paths(folder_path)
#
# # 打印输出所有找到的图片路径
# print(image_paths)
# # for path in image_paths:
# #     print(path)

#
# import os
#
# def get_image_paths(folder_path):
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
#     image_paths = []
#
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if any(file.lower().endswith(ext) for ext in image_extensions):
#                 image_paths.append(os.path.join(root, file))
#
#     return image_paths
#
# # 示例用法
# folder_path = r'D:\shixun\sss\Test'  # 注意这里使用了原始字符串(r'')来处理反斜杠转义问题
# image_paths = get_image_paths(folder_path)
#
# # 提取不带后缀的文件名部分
# file_names_no_extension = [os.path.splitext(os.path.basename(path))[0] for path in image_paths]
#
# # 打印输出所有找到的图片文件名（不带后缀）
# print(file_names_no_extension)
# # print(len(file_names_no_extension))


import os

def get_txt_paths_by_time(folder_path):
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

# 示例用法
# folder_path = '/path/to/your/folder'
folder_path = r'D:\shixun\sss\runs\detect\predict4\labels'
sorted_txt_paths = get_txt_paths_by_time(folder_path)
print(sorted_txt_paths)