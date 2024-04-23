import os
import shutil
import random

def copy_files_with_labels(img_folder, label_folder, output_img_folder, output_label_folder, max_files=1500):
    """
    随机复制图片及其对应的标签文件到新文件夹。
    :param img_folder: 包含原始图片的文件夹路径
    :param label_folder: 包含标签文件的文件夹路径
    :param output_img_folder: 保存复制图片的目标文件夹路径
    :param output_label_folder: 保存复制标签文件的目标文件夹路径
    :param max_files: 最大复制文件数量
    """
    # 确保输出文件夹存在，不存在则创建
    os.makedirs(output_img_folder, exist_ok=True)
    os.makedirs(output_label_folder, exist_ok=True)

    # 获取所有jpg文件并随机选择
    image_files = [f for f in os.listdir(img_folder) if f.endswith('.jpg')]
    selected_files = random.sample(image_files, min(max_files, len(image_files)))

    # 复制选定的图片和对应的标签文件
    for filename in selected_files:
        img_path = os.path.join(img_folder, filename)
        label_path = os.path.join(label_folder, filename.replace('.jpg', '.txt'))

        # 复制图片
        shutil.copy(img_path, os.path.join(output_img_folder, filename))
        # 复制对应的标签文件
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_label_folder, filename.replace('.jpg', '.txt')))
        else:
            print(f"Label file for {filename} does not exist.")

        print(f'Copied {filename} and its label')

# 使用函数
source_img_folder = 'D:/datasets/images/train'
source_label_folder = 'D:/datasets/labels/train'
destination_img_folder = 'D:/datasets/cut_images'
destination_label_folder = 'D:/datasets/cut_label'
copy_files_with_labels(source_img_folder, source_label_folder, destination_img_folder, destination_label_folder)
