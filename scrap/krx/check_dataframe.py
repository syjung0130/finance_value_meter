import pandas as pd

file_path = 'C:/Users/SYJ/Downloads/data.csv'
data_frame = pd.read_csv(file_path)

print(data_frame.shape)

print('===== row =====')
print(data_frame.iloc[0])

print('\n===== column =====')
print(data_frame['EPS'][0])
print('=====================')
print(data_frame['종목명'][0])


print('\n===== column(loc) =====')
print(data_frame.loc[0]['EPS'])
print('=====================')
print(data_frame.loc[0]['종목명'])

print("\n===== check 11111=====")
dfb = data_frame[data_frame['종목명']=='삼성전자'].index.values.astype(int)[0]
print(dfb)

print("\n===== check 22222 =====")
a = data_frame[data_frame['종목명']=='삼성전자']
print(a)

print('\n\n======== total data frame ========')
print(data_frame)