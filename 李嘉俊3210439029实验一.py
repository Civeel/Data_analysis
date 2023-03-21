import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('F:/titanic_train.csv')
print(df.describe())
print(df.head(10))
AgeValue = df['Age']
AgeNullValue = AgeValue.isnull().sum()
print(len(AgeValue) - AgeNullValue)
print(np.mean(AgeValue))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
p = df[['Age', 'Fare']].boxplot(return_type='dict')
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / y[i], y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
plt.show()

