import os
import shutil


def copy_files_with_labels(img_folder, label_folder, output_img_folder, output_label_folder, max_files=2000):
    """
    复制图片及其对应的标签文件到新文件夹。
    :param img_folder: 包含原始图片的文件夹路径
    :param label_folder: 包含标签文件的文件夹路径
    :param output_img_folder: 保存复制图片的目标文件夹路径
    :param output_label_folder: 保存复制标签文件的目标文件夹路径
    :param max_files: 最大复制文件数量
    """
    # 确保输出文件夹存在，不存在则创建
    os.makedirs(output_img_folder, exist_ok=True)
    os.makedirs(output_label_folder, exist_ok=True)

    count = 0
    for filename in sorted(os.listdir(img_folder)):
        if filename.endswith('.jpg') and count < max_files:
            img_path = os.path.join(img_folder, filename)
            label_path = os.path.join(label_folder, filename.replace('.jpg', '.txt'))

            # 复制图片
            shutil.copy(img_path, os.path.join(output_img_folder, filename))
            # 复制对应的标签文件
            shutil.copy(label_path, os.path.join(output_label_folder, filename.replace('.jpg', '.txt')))

            print(f'Copied {filename} and its label')
            count += 1


# 使用函数
source_img_folder = 'D:/datasets/images'
source_label_folder = 'D:/datasets/label'
destination_img_folder = 'D:/datasets/noise_images'
destination_label_folder = 'D:/datasets/noise_label'
copy_files_with_labels(source_img_folder, source_label_folder, destination_img_folder, destination_label_folder)

