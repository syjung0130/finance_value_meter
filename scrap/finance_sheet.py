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
    
    def get_finance_sheet(self, name):
        print("get_finance_sheet")
        # 회사 검색
        corp = self.find_by_corp_name(name)
        
        # 2012년부터 연간 연결재무제표 불러오기
        # TODO: date 표기법 통일 및 전달인자 처리 필요
        fs = corp.extract_fs(bgn_de='20170101')
        
        # 재무제표 검색 결과를 엑셀파일로 저장 ( 기본저장위치: 실행폴더/fsdata )
        fs.save()


if __name__ == "__main__":
    # print("check finance data")
    finance_data = FinanceSheet()
    finance_data.get_finance_sheet('삼성전자')
