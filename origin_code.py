import numpy as np
import matplotlib as mpl
import pandas as pd
import os


file_path = "Table.txt"
_, ext = os.path.splitext(file_path)
if ext == ".txt":
    # 获取第一行作为表头,剩下的作为数据
    with open(file_path, "r") as f:
        header = f.readline()
        print(header)
        data =  f.readlines()
        print(data)

