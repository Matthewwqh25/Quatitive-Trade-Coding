import os
import numpy as np
import matplotlib as mpl
import pandas
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

class StockAnalysis:
    def get_data(self, file_path: str):
        """
        :param file_path: 导入的数据，一般为某个特定股票的近两年数据
        :return: dataframe: 处理好的数据框架，表头分别为：时间、开盘、最高、最低、收盘	、涨幅、振幅、总手、金额、换手%、成交次数
        """

        _, ext = os.path.splitext(file_path)
        if ext == ".txt":
            # 正常处理
            with open(file_path, "r") as f:
                # 处理表头
                header = f.readline()
                header_list = header.split()
                # 处理数据
                data_origin = f.readlines()
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

        return df

    def calculate_range_bydays(self, df: pandas.DataFrame):
        df['极差'] = df['最高'] - df['最低']
        return df

    def calculate_SMA(self, df: pandas.DataFrame, window_size=5):
        df['SMA'] = df['收盘'].rolling(window=window_size).mean()
        df['SMA_week'] = df['收盘'].rolling(window=5).mean()
        df['SMA_month'] = df['收盘'].rolling(window=20).mean()
        df['SMA_year'] = df['收盘'].rolling(window=250).mean()
        return df

    def calculate_EMA(self, df: pandas.DataFrame, window_size=5):
        df['EMA'] = df['收盘'].ewm(span=window_size, adjust=False).mean()
        df['EMA_week'] = df['收盘'].ewm(span=5, adjust=False).mean()
        df['EMA_month'] = df['收盘'].ewm(span=20, adjust=False).mean()
        df['EMA_year'] = df['收盘'].ewm(span=250, adjust=False).mean()
        return df

    def calculate_MACD(self, df: pandas.DataFrame):


if __name__ == '__main__':
    path = "Table.txt"
    a1 = StockAnalysis()
    a1_df = a1.get_data(path)
    a1_df = a1.calculate_range_bydays(a1_df)
    a1_df = a1.calculate_SMA(a1_df)
    a1_df = a1.calculate_EMA(a1_df)



    # # 创建画布和子图
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # fig, ax = plt.subplots(figsize=(12, 6))
    #
    # # 绘制线条：收盘价+三条均线（区分颜色和线型）
    # ax.plot(a1_pd['时间'], a1_range, color='#1f77b8', linewidth=1.5, label='极差', alpha=0.8)
    # # ax.plot(a1_pd['时间'], a1_pd['收盘'], color='#1f77b4', linewidth=1.5, label='收盘价', alpha=0.8)
    # # ax.plot(a1_pd['时间'], a1_SMA_week, color='#ff7f0e', linewidth=1.2, label='5日均线', alpha=0.8)
    # # ax.plot(a1_pd['时间'], a1_SMA_month, color='#2ca02c', linewidth=1.2, label='20日均线', alpha=0.8)
    # # ax.plot(a1_pd['时间'], a1_SMA_year, color='#d62728', linewidth=1.2, label='250日均线', alpha=0.8)
    # ax.plot(a1_pd['时间'], a1_EMA_week, color='#ff7f0e', linewidth=1.2, label='5日EMA', alpha=0.8)
    # ax.plot(a1_pd['时间'], a1_EMA_month, color='#2ca02c', linewidth=1.2, label='20EMA', alpha=0.8)
    # ax.plot(a1_pd['时间'], a1_EMA_year, color='#d62728', linewidth=1.2, label='250EMA', alpha=0.8)
    #
    # # 设置x轴时间格式
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 日期格式：年-月-日
    # ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # 每月显示一个刻度
    # plt.xticks(rotation=45)  # 旋转x轴标签，避免重叠
    #
    # # 设置图表样式
    # ax.set_title('股票收盘价与移动平均线(SMA)走势图', fontsize=14, pad=20)
    # ax.set_xlabel('时间', fontsize=12)
    # ax.set_ylabel('价格（元）', fontsize=12)
    # ax.grid(True, linestyle='--', alpha=0.5)  # 添加网格线
    # ax.legend(loc='upper left', fontsize=10)  # 显示图例
    #
    # # 调整布局（避免标签被截断）
    # plt.tight_layout()
    #
    # # 显示图表
    # plt.show()