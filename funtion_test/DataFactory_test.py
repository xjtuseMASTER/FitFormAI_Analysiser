"""
input： csv
output： 绘制曲线图，需要包含原始波形，最后生成的波形
"""

import unittest
import numpy as np
import csv
from ..tasks import DataFactory, WaveData

class TestDataFactory(unittest.TestCase):
    def setUp(self):
        # 创建一个临时的 CSV 文件用于测试
        self.test_csv_data = r"E:\算法\项目管理\FitFormAI\仰卧起坐-侧面视角-单侧发力起坐(1).csv"
        self.dataFactory = DataFactory(self.test_csv_data)

    def test_setDataWave(self):
        waveData = self.dataFactory.getWaveData()
        print(waveData['dataNameList'])
        

if __name__ == '__main__':
    unittest.main()