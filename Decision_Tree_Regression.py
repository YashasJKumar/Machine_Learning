import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Sample data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([1, 4, 3, 5, 6, 7, 8, 10, 9, 10])

# Fit the decision tree regressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Predicting a new result
X_test = np.arange(min(X), max(X), 0.01)  # for higher resolution and smoother curve
X_test = X_test.reshape((len(X_test), 1))
y_pred = regressor.predict(X_test)

# Visualizing the Decision Tree Regression results
plt.scatter(X, y, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.title('Decision Tree Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
