import os
from PIL import Image

def convert_to_webp(input_path, output_path, quality=80, lossless=False):
    try:
        with Image.open(input_path) as img:
            # 保存为 WebP 格式并指定质量和是否无损
            img.save(output_path, 'WebP', quality=quality, lossless=lossless)
            print(f"{input_path} is converted to WebP at {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def convert_folder_images_to_webp(folder_path, output_folder_path, quality=80, lossless=False):
    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()

            # 检查文件扩展名是否为支持的图片格式
            if file_extension in ['.jpg', '.jpeg', '.png']:
                input_path = os.path.join(root, file)
                # 构建输出路径，将文件保存到指定的 output_folder_path
                output_path = os.path.join(output_folder_path, file_name + ".webp")
                convert_to_webp(input_path, output_path, quality=quality, lossless=lossless)

# 设置输入文件夹路径和输出文件夹路径
input_folder_path = './input_images'
output_folder_path = './output_images'

# 调用函数进行批量转换
convert_folder_images_to_webp(input_folder_path, output_folder_path)
