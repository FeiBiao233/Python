import os
import pandas as pd

# 定义要转换的文件夹路径
folder_path = r"D:\Files\工大开学\大二下\Transmission Shaft Project\实验数据\5度安装"

# 检查文件夹路径是否存在
if not os.path.exists(folder_path):
    print("文件夹路径不存在！")
    exit()

# 循环遍历文件夹中的每个文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        # 构建txt文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        
        # 读取txt文件并转换为DataFrame
        with open(file_path, 'r') as f:
            lines = f.readlines()
            data = [line.strip().split('\t') for line in lines]  # 假设每行以制表符分隔
            df = pd.DataFrame(data)
        
        # 构建Excel文件的路径
        excel_file_path = os.path.splitext(file_path)[0] + '.xlsx'
        
        # 将DataFrame写入Excel文件
        df.to_excel(excel_file_path, index=False, header=False)  # 如果不想在Excel中包含索引和列名，请将index和header参数设置为False
        print(f"已将 {file_name} 转换为 {excel_file_path}")

print("转换完成！")
