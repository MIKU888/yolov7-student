import os
import shutil
import random


def move_random_files_with_labels(img_folder, label_folder, output_img_folder, output_label_folder, percentage=0.3):
    """
    随机移动指定百分比的图片及其对应的标签文件到新文件夹。
    :param img_folder: 包含原始图片的文件夹路径
    :param label_folder: 包含标签文件的文件夹路径
    :param output_img_folder: 保存剪切图片的目标文件夹路径
    :param output_label_folder: 保存剪切标签文件的目标文件夹路径
    :param percentage: 要移动的文件占总文件的百分比
    """
    # 确保输出文件夹存在，不存在则创建
    os.makedirs(output_img_folder, exist_ok=True)
    os.makedirs(output_label_folder, exist_ok=True)

    # 获取所有jpg文件
    all_images = [f for f in os.listdir(img_folder) if f.endswith('.jpg')]
    # 随机选择指定百分比的图片
    num_files_to_move = int(len(all_images) * percentage)
    selected_files = random.sample(all_images, num_files_to_move)

    # 移动选定的图片和对应的标签文件
    for img_filename in selected_files:
        base_name = os.path.splitext(img_filename)[0]  # 去除扩展名，获取基本文件名
        img_path = os.path.join(img_folder, img_filename)
        label_path = os.path.join(label_folder, base_name + '.txt')

        # 移动图片
        shutil.move(img_path, os.path.join(output_img_folder, img_filename))
        # 移动标签文件
        shutil.move(label_path, os.path.join(output_label_folder, base_name + '.txt'))

        print(f'Moved {img_filename} and {base_name}.txt')


# 使用函数
source_img_folder = 'D:/datasets/noise_image'
source_label_folder = 'D:/datasets/noise_label'
destination_img_folder = 'D:/datasets/val/images'
destination_label_folder = 'D:/datasets/val/label'
move_random_files_with_labels(source_img_folder, source_label_folder, destination_img_folder, destination_label_folder)
