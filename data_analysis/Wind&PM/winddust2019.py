import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data loading (replace with actual paths to your CSV files)
weather_data = pd.read_csv('/home/kyy/2023_고급웹프로그래밍/data_analysis/Wind&PM/data/asos/SURFACE_ASOS_108_HR_2019_2019_2020.csv')
pm_data = pd.read_csv('/home/kyy/2023_고급웹프로그래밍/data_analysis/Wind&PM/data/pm10/ENV_YDST_108_HR_2019_2019_2020.csv')

# Wind direction conversion function
def convert_wind_direction(degree):
    if degree >= 348.75 or degree < 11.25:
        return 'N'
    elif 11.25 < degree < 33.75:
        return 'NNE'
    elif 33.75 < degree < 56.25:
        return 'NE'
    elif 56.25 < degree < 78.75:
        return 'ENE'
    elif 78.75 < degree < 101.25:
        return 'E'
    elif 101.25 < degree < 123.75:
        return 'ESE'
    elif 123.75 < degree < 146.25:
        return 'SE'
    elif 146.25 < degree < 168.75:
        return 'SSE'
    elif 168.75 < degree < 191.25:
        return 'S'
    elif 191.25 < degree < 213.75:
        return 'SSW'
    elif 213.75 < degree < 236.25:
        return 'SW'
    elif 236.25 < degree < 258.75:
        return 'WSW'
    elif 258.75 < degree < 281.25:
        return 'W'
    elif 281.25 < degree < 303.75:
        return 'WNW'
    elif 303.75 < degree < 326.25:
        return 'NW'
    elif 326.25 < degree < 348.75:
        return 'NNW'
    else:
        return None  # Or some default value for unexpected cases


# Convert wind direction from degrees to cardinal directions
weather_data['Wind Direction'] = weather_data['풍향(16방위)'].apply(convert_wind_direction)

# Merge datasets on date column (assuming '일시' is the common date column)
data_merged = pd.merge(weather_data, pm_data, on='일시')

# Calculate average PM10 concentration by wind direction
wind_pm_avg = data_merged.groupby('Wind Direction')['1시간평균 미세먼지농도(㎍/㎥)'].mean().reset_index()

# Map the wind directions to their respective positions on the plot
directions_order = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
wind_pm_avg['Wind Direction'] = pd.Categorical(wind_pm_avg['Wind Direction'], categories=directions_order, ordered=True)
wind_pm_avg = wind_pm_avg.sort_values('Wind Direction')

# Create a polar plot
theta = np.linspace(0.0, 2 * np.pi, 16, endpoint=False)
radii = wind_pm_avg['1시간평균 미세먼지농도(㎍/㎥)']
width = np.pi / 8 * np.ones_like(theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Set the compass labels
ax.set_xticks(theta)
ax.set_xticklabels(directions_order)

plt.show()
