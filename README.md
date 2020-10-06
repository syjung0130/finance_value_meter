# 기업의 적정 주가 측정
## 종목별 현재 지수 측정
 - 단일 종목의 PER, PBR, ROE 지수의 추세를 확인 및 측정    
 - BPS, PBR, EPS, PER, ROE  
 - krx 데이터를 사용  
## 종목별 적정 주가 측정
 - ROE를 기반으로 적정 주가를 측정
 - ROE가 비정상적으로 낮거나 높을 경우, 정상적인 측정이 불가함.  
 (PER과 ROE가 10이상 차이가 나면 정상적인 측정이 불가함.  
 ROE는 자본대비 이익율인데, 생산시설 등이 커서 자본이 큰 경우가 있고,  
 자본이 비정상적으로 작거나 매출이 너무 낮은 경우(스타트업) 정확한 측정이 불가능하다.  
 )  
  
-----------------------
# 실행 방법  
-----------------------
## 공통  
-----------------------
### 크롬 버전 확인  
크롬 열고 chrome://version 입력  
  
### chromedriver 다운로드
아래 url에서 chrome 버전에 일치하는 chromedriver.exe를 다운로드 한다.  
https://sites.google.com/a/chromium.org/chromedriver/downloads  
  
### chromedriver를 프로그램 디렉토리로 복사  
다운로드 받은 chromedriver.exe를 프로그램 디렉토리로 복사  
  
## develop 버전 실행 방법  
-----------------------  
### virtualenv 설치  
pip install virtualenv  
vscode 관리자 권한으로 실행 -> ctrl + ' -> (powershell)  
virtualenv venv  
.\venv\Scripts\activate  
  
### 설치 패키지 목록  
python -m pip install PyQt5==5.13 PyQtChart==5.13  
pip install pandas  
pip install dart_fss  
pip install selenium  
  
### 실행  
python main.py  
  
  
## release 버전 실행 방법  
------------------------  
실행파일 실행(value_meter.exe)  
  