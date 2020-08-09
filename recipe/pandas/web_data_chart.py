import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt


# dataframe을 사용하기 위해서는 pandas패키지를 설치해야한다.
# pip install pandas
# pip install matplotlib

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 5, 29)

gs = web.DataReader("078930.KS", "yahoo", start, end)
gs.info()
# 종가 차트를 그린다.
# plt.plot(gs['Adj Close'])
# plt.show()

# print(gs.index)
# plt.plot(gs.index, gs['Adj Close'])
# plt.show()
# ma5 = gs['Adj Close'].rolling(window=5).mean()
# print('Mean Average value in Last 10 days')
# print(ma5.tail(10))

# 휴일데이터를 제거한 뒤, 이동평균선을 구해서 dataframe의 컬럼에 추가한다.
new_gs = gs[gs['Volume'] !=0]
new_gs.tail(5)
ma5 = new_gs['Adj Close'].rolling(window=5).mean()
print('Mean Average value in Last 10 days')
print(ma5.tail(10))
new_gs.insert(len(new_gs.columns), "MA5", ma5)

ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

print('Mean Average value in Last 10 days')
print(new_gs.tail(5))

# 종가 그래프
plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')
plt.plot(new_gs.index, new_gs['MA5'], label = "MA5")
plt.plot(new_gs.index, new_gs['MA20'], label = "MA20")
plt.plot(new_gs.index, new_gs['MA60'], label = "MA60")
plt.plot(new_gs.index, new_gs['MA120'], label = "MA120")

plt.legend(loc="best")
plt.grid()
plt.show()

print(new_gs.index)