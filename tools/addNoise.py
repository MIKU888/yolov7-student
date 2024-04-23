import os
from PIL import Image
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):
    """
    向图像添加高斯噪声
    :param image: PIL图像对象
    :param mean: 噪声的均值
    :param sigma: 噪声的标准差
    :return: 带噪声的图像对象
    """
    image_np = np.array(image)
    noise = np.random.normal(mean, sigma, image_np.shape)
    image_np_noisy = image_np + noise
    image_np_noisy = np.clip(image_np_noisy, 0, 255)  # 限制像素值在0-255之间
    return Image.fromarray(image_np_noisy.astype('uint8'))

def process_images(folder_path, output_folder):
    """
    批量处理目录中的图像，为它们添加高斯噪声
    :param folder_path: 包含原始图像的目录路径
    :param output_folder: 保存带噪声图像的目录路径
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(('jpg', 'jpeg', 'png')):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            noisy_image = add_gaussian_noise(image)
            noisy_image.save(os.path.join(output_folder, filename))
            print(f'Processed {filename}')

# 使用函数
source_folder = 'D:/datasets/noise_images'
output_folder = 'D:/datasets/noise_image'
process_images(source_folder, output_folder)
