import pandas as pd

class StockCode:
    def __init__(self):
        print("__init__")
    
    def get_code_list(self):
        print("get_code_list")
        self.df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
        print(self.df.head())