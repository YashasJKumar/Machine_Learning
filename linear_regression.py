import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

data = pd.read_csv('Datasets/headbrain.csv')
print(data.shape)
print(data.head())

# collecting X & Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

# mean of x n y

mean_x = np.mean(X)
mean_y = np.mean(Y)
# total number of values
n = len(X)

numer = 0
denom = 0

for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2

m = numer / denom
c = mean_y - (m * mean_x)

print(m, c)

# Plotting Values and Regression Line
# setting the limits of the x and y-axis of the plot, the 100 is added to make all the points visible

max_x = np.max(X) + 100
min_x = np.min(X) - 100
# Calculating line values x and y
# make a linear space of 1000 evenly spaced numbers from min_x to max_x

x = np.linspace(min_x, max_x, 1000)  # this is used to plot the x-axis of the regression line

y = c + m * x

# Plotting Line
plt.plot(x, y, color='#52b920', label='Regression Line')
# Plotting Scatter Points
plt.scatter(X, Y, c='#ef4423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

ss_t = 0
ss_r = 0
for i in range(n):
    y_pred = c + m * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2

r2 = 1 - (ss_r / ss_t)
print(r2)



