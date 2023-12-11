import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
data = pd.read_csv('/home/kyy/2023_고급웹프로그래밍/data_analysis/China&PM/data/beijing_seoul_finedust2019.csv')

# 데이터 탐색
print("Data Head:")
print(data.head())

# 데이터 시각화
plt.figure(figsize=(12, 6))
sns.lineplot(x='month', y='beijing_pm10', data=data, label='Beijing PM10', marker='o')
sns.lineplot(x='month', y='seoul_pm10', data=data, label='Seoul PM10', marker='o')
plt.title('2020 Monthly Average PM10 Levels in Beijing and Seoul')
plt.xlabel('Month')
plt.ylabel('Average PM10 Level')
plt.xticks(range(1, 13))  # 월별로 x축 표시
plt.legend()
plt.show()

# 상관관계 계산
correlation = data[['beijing_pm10', 'seoul_pm10']].corr(method='pearson')
print('2018 Correlation between Beijing and Seoul PM10 levels:')
print(correlation)
