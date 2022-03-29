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