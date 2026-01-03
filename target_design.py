import os
import numpy as np
import matplotlib as mpl
import pandas as pd

class StockAnalysis:
    def get_data(self, file_path: str) -> pd.DataFrame:
        """
        :param file_path: 文件路径
        :return: pandas DataFrame
        """
        _, ext = os.path.splitext(file_path)
        if ext == ".txt":
            # 获取第一行作为表头
            with open(file_path, "r") as f:
                header = f.readline()
        return df
