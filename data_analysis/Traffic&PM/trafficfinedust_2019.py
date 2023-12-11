import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 데이터 불러오기
daily_air = pd.read_csv('/home/kyy/2023_고급웹프로그래밍/data_analysis/Traffic&PM/data/2019_daily_air_quality.csv')
daily_traffic = pd.read_csv('/home/kyy/2023_고급웹프로그래밍/data_analysis/Traffic&PM/data/2019_daily_traffic.csv')

# 'Unnamed: 0' 열 제거
daily_air = daily_air.drop('Unnamed: 0', axis=1)
daily_traffic = daily_traffic.drop('Unnamed: 0', axis=1)

# '일자' 열 형식을 일치시키기
daily_air['일자'] = pd.to_datetime(daily_air['일자'], format='%Y-%m-%d')
daily_traffic['일자'] = pd.to_datetime(daily_traffic['일자'], format='%Y%m%d')

# 데이터 병합
merged_data = pd.merge(daily_air, daily_traffic, on='일자')
print(merged_data.isnull().sum())

# NaN 값을 0으로 대체
merged_data.fillna(0, inplace=True)

# 2019 상관관계 분석 - 피어슨의 상관계수 이용
corr, _ = pearsonr(merged_data['pm10'], merged_data['교통량합계'])

# 산점도 그리기
plt.scatter(merged_data['pm10'], merged_data['교통량합계'], c='lightgreen')  # 점 색상을 파란색으로 지정
plt.xlabel('finedust')
plt.ylabel('traffic')
plt.title('2019')
plt.show()

# 상관계수 출력
print(f'2019 상관계수 (피어슨): {corr:.4f}')
