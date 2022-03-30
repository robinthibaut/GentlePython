#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Let's learn about linear regression with scikit-learn!

# The dataset we'll use for this partial least squares regression
# exercise is a very common one used for regression examples.
# It is the Boston Housing Dataset and contains information about the housing values in suburbs of Boston.

from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.datasets import load_boston

# prepare the data
boston = load_boston()

X = boston.data
y = boston.target

print(X.shape)
print(y.shape)

# X.shape is (506, 13), which means we have 506 answers for 13 predictors
# y.shape is (506,), which means we have 506 answers for the target

boston.feature_names

# Total transcripts
print(boston['DESCR'])

# Fit a linear regression model

from sklearn.model_selection import train_test_split

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train, y_train)

# Predict

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()

# Let's evaluate our model:

# Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error.
# Refer to the lecture or to Wikipedia for the formulas

import numpy as np

# mean absolute error
mae = metrics.mean_absolute_error(y_test, predictions)

# mean squared error
mse = metrics.mean_squared_error(y_test, predictions)

# root mean squared error
rmse = np.sqrt(metrics.mean_squared_error(y_test, predictions))

# print them out
print(mae)
print(mse)
print(rmse)
