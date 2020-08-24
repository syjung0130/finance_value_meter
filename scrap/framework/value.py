# 아래 중 하나의 값을 저장한다.
# (섹터 타입) 리스트
# (섹터 타입, 종목리스트) 섹터에 해당하는 종목 딕셔너리
# BPS (종목, BPS)딕셔너리
# PBR (종목, PBR)딕셔너리
# EPS (종목, EPS)딕셔너리
# PER (종목, PER)딕셔너리
# ROE (종목, ROE)딕셔너리
class Value:
    def __init__(self, value_type):
        print("__init__")
        self.value_type = value_type

    def print_value(self):
        print("수집된 데이터 출력")

    def set_value(self, list):
        self.list = list

    def get_value(self):
        return self.list