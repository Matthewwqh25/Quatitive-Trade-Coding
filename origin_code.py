import numpy as np
import matplotlib as mpl
import pandas as pd
import os


file_path = "Table.txt"
_, ext = os.path.splitext(file_path)
if ext == ".txt":
    with open(file_path, "r") as f:
        # 处理表头
        header = f.readline()
        header_list = header.split()
        # 处理数据
        data_origin =  f.readlines()
        # 移除每行末尾的换行符
        data_move_t = [line.rstrip() for line in data_origin]
        # 移除空行
        data_move_empty_line = [line for line in data_move_t if line.strip()]
        # 将每行内的数据根据空格分割
        data_lines = [line.split() for line in data_move_empty_line]
        df = pd.DataFrame(data_lines, columns=header_list)
        print(df)
        # print(data_lines)

        # for line in data_move_empty_line:
        #     print(line.split())
        #     print(len(line.split()))

        # data_list = []
        # for line in data:
        #     print(line.strip())
        #     data_list.append(line.strip())
        # print(data_list)
        # for line in data:
        #     if line
        #     print(line.splitlines())
        # print(data)
        # print(type(data))



