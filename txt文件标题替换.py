import os

# 指定目录路径
dir_path = "D:/Python_Program/WNovelArchiver/novel_list/恋人・交换 - 副本"

# 遍历目录中的所有文件
for filename in os.listdir(dir_path):
    # 只处理txt文件
    if filename.endswith(".txt"):
        # 读取文件内容
        with open(os.path.join(dir_path, filename), "r", encoding='UTF8') as f:
            content = f.read().splitlines()
        # 将第一行作为标题
        number = filename.split('_', 1)[0] + '_'
        title = content[0]
        # 将标题写入文件名
        new_filename = os.path.join(dir_path, number + title + ".txt")
        # 重命名文件
        os.rename(os.path.join(dir_path, filename), new_filename)
