#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mean = np.array([0, 0, 0])
cov = np.array([[1, -0.5, -0.2], [-0.5, 1., 0], [-0.2, 0, 1]])  # Randomly selected covariance matrix
class1 = np.random.multivariate_normal(mean, cov,
                                       100)  # 100 randomly selected points from a multivariate normal distribution
class2 = np.random.multivariate_normal(mean + 0.8, cov + 0.3, 80)  # 80 randomly selected points with a shifted mean
labels = [0] * 100 + [1] * 80  # Labels for the classes
data = np.concatenate([class1, class2])  # Combining the two classes

# Plotting the data in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=labels)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

N = 2
# Calculate the eigen values and vectors of the co-variance matrix of the data.
mean = np.mean(data, axis=0)
centered_data = data - mean

cov_matrix = np.cov(centered_data.T)
plt.imshow(cov_matrix)
plt.title('Covariance Matrix')
plt.colorbar()
plt.show()

eigenValues, eigenVectors = np.linalg.eigh(cov_matrix)

# Sort the eigenvalues from highest to lowest.
idx = np.argsort(eigenValues)[::-1]

# Get the top N eigen vectors and sort then from highest eigenvalue to lowest.
eigenVectors = eigenVectors[:, idx]
eigenVectors = eigenVectors[:, :N]

# Project the data onto the eigenvectors with the highest eigenvalues.
eigenVectors = eigenVectors.T
projection = np.dot(eigenVectors, centered_data.T)

# the explained variance is the ratio of the eigenvalues to the sum of all eigenvalues.
explained_variance = (eigenValues / np.sum(eigenValues))[idx]

plt.scatter(projection[0], projection[1], alpha=1, c=labels)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA')
plt.show()