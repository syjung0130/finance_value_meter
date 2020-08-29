import pandas as pd

class StockCode:
    def __init__(self):
        print("__init__")
    
    def update_stock_codes(self):
        print("update_stock_codes")
        self.df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
        print(self.df.head())

        self.n_rows = self.df.shape[0]
        self.n_cols = self.df.shape[1]
        print('shape: ({0}, {1})'.format(self.n_rows, self.n_cols))

        print("row: ")
        print(self.df.iloc[0])

        print("column")
        print(self.df.iloc[0]['종목코드'])
    
    def get_stock_code_by_name(self, str_name):
        print('get_stock_code_by_name')
        for i in range(self.n_rows):
            if self.df.iloc[i]['회사명'] == str_name:
                return self.df.iloc[i]['종목코드']
        raise ValueError#not exist str_name, invalid str_name

    def get_stock_name_by_code(self, str_code):
        print('get_stock_name_by_code')
        for i in range(self.n_rows):
            if self.df.iloc[i]['종목코드'] == str_code:
                return self.df.iloc[i]['회사명']
        raise ValueError#not exist str_name, invalid str_name


