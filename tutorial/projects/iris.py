"""Here is a python project for beginners using Pycharm.

In this project, we will be working with a dataset that contains information on different flowers (Iris dataset).
This dataset was created by R.A. Fisher and is available in the scikit-learn dataset library.

We will be using NumPy and Matplotlib to analyze the data and create some visualizations.
We will also be creating a custom class to store information on each flower.

You will have to set up the project yourself.

Optional: You can get familiar with VCS by enabling the "Use VCS" option in the "Project Settings" window.
Ideally, you should commit your changes to your VCS and push them to your remote repository.

The dataset contains information on the following:

* Sepal length

* Sepal width

* Petal length

* Petal width

* Species

The species are Iris setosa, Iris virginica, and Iris versicolor.

This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length,
stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

The goal of this project is to create a script that will analyze the data and create a visualization of the data.

______________________________________________________________________________________________________________

Here are the exercises you have to solve to familiarise yourself with Python using this dataset:

1. Load the dataset into a variable called `iris`.

2. Print the first 5 rows of the dataset.

3. Print the number of samples in the dataset.

4. Print the number of features in the dataset.

5. Print the names of the features in the dataset.

6. Print the species of the first 5 samples in the dataset.

7. Extract the sepal length and sepal width of the first 5 samples in the dataset and print them.

8. Extract the petal length and petal width of the first 5 samples in the dataset and print them.

9. Extract all the features for the first 5 samples in the dataset and print them.

10. Extract the sepal length of all the samples in the dataset and print them.

11. Extract the petal length of all the samples in the dataset and print them.

12. Calculate the mean, median, standard deviation, and variance of the sepal length of all the samples in the dataset.

13. Calculate the mean, median, standard deviation, and variance of the sepal width of all the samples in the dataset.

14. Calculate the mean, median, standard deviation, and variance of the petal length of all the samples in the dataset.

15. Calculate the mean, median, standard deviation, and variance of the petal width of all the samples in the dataset.

16. Plot a histogram of the sepal length of all the samples in the dataset.

17. Plot a histogram of the sepal width of all the samples in the dataset.

18. Plot a histogram of the petal length of all the samples in the dataset.

19. Plot a histogram of the petal width of all the samples in the dataset.

20. Plot a scatter plot of the sepal length and sepal width of all the samples in the dataset.

21. Plot a scatter plot of the petal length and petal width of all the samples in the dataset.

22. Plot a scatter plot matrix of all the features in the dataset.

23. Plot a boxplot of the sepal length of all the samples in the dataset.

24. Plot a boxplot of the sepal width of all the samples in the dataset.

25. Plot a boxplot of the petal length of all the samples in the dataset.

26. Plot a boxplot of the petal width of all the samples in the dataset.

27. Plot a violinplot of the sepal length of all the samples in the dataset.

28. Plot a violinplot of the sepal width of all the samples in the dataset.

29. Plot a violinplot of the petal length of all the samples in the dataset.

30. Plot a violinplot of the petal width of all the samples in the dataset.

31. Calculate the correlation matrix of all the features in the dataset.

32. Visualize the correlation matrix using a heatmap.
"""

#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

import matplotlib.pyplot as plt
from sklearn import datasets

# import some data to play with
df = datasets.load_iris()


# Create a custom class to store information on each flower
class Flower:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def __str__(self):
        return f"FLower: {self.species}, Sepal Length: {self.sepal_length}, Sepal Width: {self.sepal_width}, Petal " \
               f"Length: {self.petal_length}, Petal Width: {self.petal_width} "


# Create a function that will analyze the data and create a visualization
def analyze_data(data):
    # Create a list of flowers
    flowers = []
    for i in range(len(data.data)):
        flowers.append(Flower(data.data[i][0], data.data[i][1], data.data[i][2], data.data[i][3], data.target[i]))

    # Create a histogram of all the petal widths
    plt.subplot(1, 2, 1)
    plt.hist(data.data[:, 3])
    plt.title("Petal Width")

    # Create a scatter plot of the data that includes the sepal width and petal width of each flower
    plt.subplot(1, 2, 2)
    plt.scatter(data.data[:, 1], data.data[:, 3])
    plt.title("Sepal Width vs Petal Width")

    plt.show()


# Functions to run the script and visualize the data
def main():
    analyze_data(df)


if __name__ == "__main__":
    main()
