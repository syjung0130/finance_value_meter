import json
import dart_fss as dart


# '''
# API, 사용법에 대한 내용은 아래 url을 참고
# https://pypi.org/project/dart-fss/
# 패키지 설치는 아래 명령으로
# pip install dart-fss
# '''
class FinanceSheet():
    def __init__(self):
        print("__init__")
        with open('info.json') as json_file:
            self.json_data = json.load(json_file)

        self.dart_key = self.json_data["dart_key"]

        # Open DART API KEY 설정
        dart.set_api_key(api_key=self.dart_key)

    def get_corp_list(self):
        print("get_corp_list")
        return dart.get_corp_list()
    
    def find_by_corp_name(self, name):
        print("find_by_corp_name")
        corp_list = self.get_corp_list()
        return corp_list.find_by_corp_name(name, exactly=True)[0]

    def get_finance_excel(self, name):
        print("get_finance_excel")
        self.extract_finance_sheet(name)
        
        # 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
        self.fs.save()
    
    def update_finance_sheet(self, name):
        print("update_finance_sheet")
        self.extract_finance_sheet(name)
        
        self.update_balance_sheet()
        self.update_income_statement()
        self.update_consolidated_income_statement()
        self.update_cash_flow()
    
    def extract_finance_sheet(self, name):
        # 회사 검색
        self.corp = self.find_by_corp_name(name)
        
        # 2017년부터 연간 연결재무제표 불러오기
        # TODO: date 표기법 통일 및 전달인자 처리 필요
        self.fs = self.corp.extract_fs(bgn_de='20170101')
        return self.fs

    def update_balance_sheet(self):
        print("get_balance_sheet")
        # 연결재무상태표(Balance Sheet)
        self.df_bs = self.fs['bs'] # 또는 df = fs[0] 또는 df = fs.show('bs')
        # 연결재무상태표 추출에 사용된 Label 정보
        self.labels_bs = self.fs.labels['bs']
        print("===== 연결 재무 상태표 =====")
        print(type(self.df_bs))
        print(self.df_bs)
        print(self.labels_bs)

    def update_income_statement(self):
        # 연결손익계산서(Incom Statement)
        self.df_is = self.fs['is'] # 또는 df = fs[1] 또는 df = fs.show('is')
        # 연결손익계산서 추출에 사용된 Label 정보
        self.labels_is = self.fs.labels['is']
        print("===== 연결 손익 계산서 =====")
        print(type(self.df_is))
        print(self.df_is)
        print(self.labels_is)
    
    def update_consolidated_income_statement(self):
        # 연결포괄손익계산서(Consolidated Income Statement)
        self.df_ci = self.fs['cis'] # 또는 df = fs[2] 또는 df = fs.show('cis')
        # 연결포괄손익계산서 추출에 사용된 Label 정보
        self.labels_ci = self.fs.labels['cis']
        print("===== 연결 포괄 손익 계산서 =====")
        print(type(self.df_ci))
        print(self.df_ci)
        print(self.labels_ci)
    
    def update_cash_flow(self):
        # 현금흐름표(Cash Flow)
        self.df_cf = self.fs['cf'] # 또는 df = fs[3] 또는 df = fs.show('cf')
        # 현금흐름표 추출에 사용된 Label 정보
        self.labels_cf = self.fs.labels['cf']
        print("===== 현금 흐름표 =====")
        print(type(self.df_cf))
        print(self.df_cf)
        print(self.labels_cf)

    

if __name__ == "__main__":
    # print("check finance data")
    finance_data = FinanceSheet()
    finance_data.update_finance_sheet('삼성전자')
