import matplotlib
import numpy as np
import matplotlib as mpl
import pandas as pd
import os
from matplotlib import pyplot as plt
from matplotlib.font_manager import weight_dict
from pylab import mpl
import seaborn as sns
import tushare as ts

# dtype_list = (str, float, float, float, float, str, str, int, int)
# dtype_list = (float, str)
file_path = "Table.txt"
_, ext = os.path.splitext(file_path)
if ext == ".txt" or ext == ".csv":
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
        # 数据预处理
        df['时间'] = df['时间'].apply(lambda x: x.split(',')[0])
        df['时间'] = pd.to_datetime(df['时间'])
        df['开盘'] = df['开盘'].apply(lambda x: round(float(x), 2))
        df['最高'] = df['最高'].apply(lambda x: round(float(x), 2))
        df['最低'] = df['最低'].apply(lambda x: round(float(x), 2))
        df['收盘'] = df['收盘'].apply(lambda x: round(float(x), 2))
        # 计算每日的极差
        df['极差'] = df['最高']-df['最低']
        print(df['极差'])

        # 计算简单平均线
        df['SMA'] = df['收盘'].rolling(window=5).mean().tolist()
        print(np.round(df['SMA'].tolist(),2))











        # mpl.rcParams['axes.unicode_minus'] = False
        # # %matplotlib inline
        # sh = ts.get_k_data(code='sh',ktype='D',autype='qfq')
        # sh.head(5)
        # sh.index = pd.to_datetime(sh.date)
        # sh['close'].plot(figsize=(12,6))
        # plt.show()
        # np.loadtxt()



