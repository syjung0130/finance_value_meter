from selenium import webdriver

'''
 # chrome 버전 정보 확인: chrome://version
 # 아래 url에서 chrome 버전에 일치하는 chromedriver.exe를 다운로드 한다.
 # https://sites.google.com/a/chromium.org/chromedriver/downloads
'''
chromedriver_path = "C:/Users/SYJ/Desktop/python/chromedriver"
driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(3)
driver.get('http://marketdata.krx.co.kr/mdi#document=13020401')
driver.implicitly_wait(10)

span = driver.find_elements_by_css_selector('span.button-mdi-group button')[3]
span.click()
