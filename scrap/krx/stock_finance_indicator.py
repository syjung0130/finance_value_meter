from selenium import webdriver
import pandas as pd
import time
import datetime
import os

# 빌더 패턴 적용, 외부에서 접근할 때에는 함수 하나로 접근 가능하도록
class StockFinanceIndicator:
    def __init__(self):
        print("__init__")
    
    # 외부 접근 메서드
    def get_finance_dataframe_by_code(self, str_code):
        print("get data frame")
        self.str_code = str_code

        return self.download_statistic().\
            excel_to_pandas_dataframe().\
            get_dateframe_by_code(self.str_code)

    def download_statistic(self):
        print("PER, PBR, EPS, BPS excel sheet 다운로드")
        # download한 파일이름에 날짜를 붙여서 저장
        # 현재 날짜가 지난 날짜일 경우, 새로 download
        self.download_path = 'C:/Users/SYJ/Downloads/'#'C:/Users/SYJ/Downloads/data.csv'
        self.download_file_name = 'data.csv'

        # 업데이트하지 않아도 될 경우, download하지 않는다.
        if self.is_excel_file_already_update() == False:
            self.open_chrome_driver()
            self.do_download_excel()
            os.rename(self.download_path + self.download_file_name, self.download_path + self.excel_file_name)
        else:
            print("Excel data file is already exist.")
        
        return self

    def get_excel_full_path(self):
        return self.download_path + self.excel_file_name

    def open_chrome_driver(self):
        self.chromedriver_path = "C:/Users/SYJ/Desktop/python/chromedriver"
        self.driver = webdriver.Chrome(self.chromedriver_path)
        self.driver.implicitly_wait(3)
        self.driver.get('http://marketdata.krx.co.kr/mdi#document=13020401')
        self.driver.implicitly_wait(10)

    def is_excel_file_already_update(self):
        print(self.insert_date_to_file_name_str())
        return os.path.isfile(self.download_path + self.insert_date_to_file_name_str())

    def do_download_excel(self):
        self.span = self.driver.find_elements_by_css_selector('span.button-mdi-group button')[3]
        self.span.click()
        time.sleep(3)

    def insert_date_to_file_name_str(self):
        now = datetime.datetime.now()
        now_date = now.strftime('%Y-%m-%d')
        print(now_date)
        self.excel_file_name = self.download_file_name[:4] + "_" + now_date + self.download_file_name[4:]
        return self.excel_file_name

    def close_chrome_driver(self):
        self.driver.close()

    def excel_to_pandas_dataframe(self):# 전체 종목 data frame
        print("excel shhet -> pandas data frame")
        print("excel path : {}".format(self.get_excel_full_path()))
        self.entire_data_frame = pd.read_csv(self.get_excel_full_path())
        print(self.entire_data_frame)
        return self
    
    def get_dateframe_by_code(self, str_code):
        print("get data frame by code")
        # 전체 종목의 지표 중에서 한 종목에 대한 PER, PBR, EPS, BPS를 추출
        # ROE를 계산 후 새로운 data frame으로 생성
        # 생성된 data frame을 return
        data_frame = self.entire_data_frame[self.entire_data_frame['종목코드'] == str_code]
        print(data_frame)
        return data_frame
    
    def get_dataframe_by_name(self, str_name):
        print("get data frame by name")
        data_frame = self.entire_data_frame[self.entire_data_frame['종목명'] == '삼성전자']
        return self


if __name__ == "__main__":
    indicator = StockFinanceIndicator()
    indicator.get_finance_dataframe_by_code("005930")
