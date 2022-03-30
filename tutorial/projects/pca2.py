#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University


import matplotlib.pyplot as plt
import numpy as np

# 1. Generate some data
rng = np.random.RandomState(0)  # seed the random number generator.
# It ensures that the same data is generated every time.
n_samples = 500
cov = [[3, 3], [3, 4]]  # covariance matrix. The covariance matrix is a 2x2 matrix.
# The first row is the variance of the x-axis and the second row is the variance of the y-axis.
X = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)  # generate the data.

# 2. Calculate the covariance matrix of the data.
cov_X = np.cov(X.T)
# or
# cov_X = np.dot(X.T, X) / n_samples

# 3. Calculate eigenvectors and their corresponding eigenvalues.
eig_values, eig_vectors = np.linalg.eig(cov_X)

# 4. Sort the eigenvalues and corresponding eigenvectors from largest
# to smallest eigenvalue and select the first 2 eigenvectors.
idx = eig_values.argsort()[::-1]
eigen_values = eig_values[idx][:2]
eigen_vectors = eig_vectors[:, idx][:, :2]

# 5. Project the data onto principal components
X_transformed = np.dot(X, eigen_vectors)

# Get the explained variance ratio
explained_variance_ratio = eigen_values / np.sum(eigen_values)

# 6. Check that everything is correct with scikit-learn
from sklearn.decomposition import PCA
pca = PCA(n_components=2).fit(X)
# https://stackoverflow.com/questions/44765682/in-sklearn-decomposition-pca-why-are-components-negative
# assert np.allclose(X_transformed, pca.transform(X))
# assert np.allclose(pca.components_, eigen_vectors.T)

# 7. Plot the data
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
for i, (comp, var) in enumerate(zip(eigen_vectors.T, eigen_values)):
    comp = comp * var  # scale component by its variance explanation power
    plt.plot(
        [0, comp[0]],
        [0, comp[1]],
        label=f"Component {i}",
        linewidth=5,
        color=f"C{i + 2}",
    )
plt.gca().set(
    aspect="equal",
    title="2-dimensional dataset with principal components",
    xlabel="first feature",
    ylabel="second feature",
)
plt.legend()
# plt.savefig("pca2b.png")
plt.show()

# Run the cell above.
# You will see the eigenvectors (principal components) are visualized as lines
# that are sorted by their length.
# Each line is labeled by its number and color-coded by the type of component.
# The components are ordered by the amount of variance they explain in the data.

# Now, let's remove the most informative component from the data
# and see what happens to the data.

X2 = X_transformed.copy()
X2[:, 0] = 0  # remove the first component
X_inv = np.dot(X2, eigen_vectors.T)  # invert the transformation

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.scatter(X_inv[:, 0], X_inv[:, 1], alpha=0.3, color="orange", label="samples")
plt.gca().set(
    aspect="equal",
    title="Without the most informative component",
    xlabel="first feature",
    ylabel="second feature",
)
plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
plt.scatter(X_inv[:, 0], X_inv[:, 1], alpha=0.3)
plt.gca().set(
    aspect="equal",
    title="Original",
    xlabel="first feature",
    ylabel="second feature",
)
plt.legend()
# plt.savefig("pca2c.png")
plt.show()

# In the original data on the right, you can see the first feature
# is highly correlated with the second feature, but it is still
# possible to distinguish the samples. However, in the
# data after removing the most informative component from the left,
# the data are distributed along a single dimension,
# and you can't see any correlations between the features.

X3 = X_transformed.copy()
X3[:, 1] = 0  # remove the second component
X_inv = np.dot(X3, eigen_vectors.T)  # invert the transformation

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.scatter(X_inv[:, 0], X_inv[:, 1], alpha=0.3, color="orange", label="samples")
plt.gca().set(
    aspect="equal",
    title="Without the second most informative component",
    xlabel="first feature",
    ylabel="second feature",
)
plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
plt.scatter(X_inv[:, 0], X_inv[:, 1], color="orange", alpha=0.3)
plt.gca().set(
    aspect="equal",
    title="Original",
    xlabel="first feature",
    ylabel="second feature",
)
plt.legend()
# plt.savefig("pca2d.png")
plt.show()

# Compare with linear regression just for fun
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X[:, 0].reshape(-1, 1), X[:, 1].reshape(-1, 1))
predictions = lm.predict(X[:, 0].reshape(-1, 1))
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
plt.plot(X[:, 0], predictions.reshape(-1), color="orange", label="linear regression")
plt.scatter(X_inv[:, 0], X_inv[:, 1], color="green", alpha=0.3, label="1PC")

plt.gca().set(
    aspect="equal",
    title="Linear regression",
    xlabel="first feature",
    ylabel="second feature",
)
plt.legend(loc="upper left")
# plt.savefig("pca2e.png")
plt.show()
