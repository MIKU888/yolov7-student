import os


def add_m_to_filenames_preserve_extension(directory):
    # 检查文件夹路径是否存在
    if not os.path.exists(directory):
        print("指定的目录不存在")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(directory):
        # 构建完整的文件路径
        old_file_path = os.path.join(directory, filename)

        # 只有在文件名中不是目录时才进行重命名
        if os.path.isfile(old_file_path):
            # 分离文件名和后缀
            base, extension = os.path.splitext(filename)
            # 构建新的文件名和路径，不改变后缀
            new_filename = base + 'm' + extension
            new_file_path = os.path.join(directory, new_filename)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"文件 {filename} 已重命名为 {new_filename}")


# 使用示例：
# 请将 'path_to_your_directory' 替换为您的文件夹路径
# add_m_to_filenames_preserve_extension('path_to_your_directory')

add_m_to_filenames_preserve_extension('D:/datasets/noise_label')