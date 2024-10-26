import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Ice Cream Ratings.csv")
df.set_index('Date', inplace=True)

## print(plt.style.available)
## plt.style.use('...')

## Line chart
df.plot(kind='line', title='Ice Cream Ratings', xlabel='Daily Ratings', ylabel='Scores')
plt.show()

## Stacked bar chart, df.plot.barh for horizontal
df['Flavor Rating'].plot(kind='bar', stacked='True')
plt.show()

## Scatter plot over particular flavor and texture ratings with size 500 and color yellow
df.plot.scatter(x='Texture Rating', y='Overall Rating', s=500, c='Yellow')
plt.show()

## Histogram
## bins=a number like 10 as the number of points on x axis
df.plot.hist()
plt.show()

## Box plot
df.boxplot()
plt.show()

## Area plot with set figure size
df.plot.area(figsize=(10, 5))
plt.show()

## Pie chart
df.plot.pie(y='Flavor Rating')
plt.show()
