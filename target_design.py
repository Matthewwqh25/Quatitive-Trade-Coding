import os
import numpy as np
import matplotlib as mpl
import pandas as pd

class StockAnalysis:
    def get_data(self, file_path: str) -> pd.DataFrame:
        """
        :param file_path: 导入的数据，一般为某个特定股票的近两年数据
        :return: dataframe: 处理好的数据框架，表头分别为：时间、开盘、最高、最低、收盘	、涨幅、振幅、总手、金额、换手%、成交次数
        """
        _, ext = os.path.splitext(file_path)
        if ext == ".txt":
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
        return df
