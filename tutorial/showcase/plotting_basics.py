#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part is an introduction to plotting basic figures with Matplotlib. It's a must-see!

import matplotlib.pyplot as plt

# A. Simple scatter plots
############################
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # create an axes

# method 1: plot with plain python list
x = [1, 2, 3]
y = [2, 4, 6]
ax.plot(x, y)  # plot
plt.show()  # show the figure

# method 2: plot with numpy array
import numpy as np

x = np.array(x)  # convert to numpy array
y = np.array(y)
ax.plot(x, y)  # same as before
plt.show()

# method 3: scatter with numpy array
x = np.arange(
    1, 11
)  # use numpy function 'arange' to generate the  data points starting from 1 to 10 with the interval of 1
y = x**2  # x squared
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # add a set of axes to the figure
ax.scatter(x, y)  # draw the scatter plot with labels of x and y separately
ax.scatter(x, y, c="r", marker="*")  # add some attributes to the plot
ax.set_xlabel("X")  # set the x-axis label
ax.set_ylabel("$y=x^2$")  # set the y-label including symbols like $ y = x ^ 2 $
ax.set_title("scatter plot with matplotlib")  # set the title
plt.show()  # show the figure

# method 3: scatter  with numpy array (make marker larger and color darker)
x = np.arange(
    1, 11
)  # use numpy function 'arange' to generate the  data points starting from 1 to 10 with the interval of 1
y = x**2  # x squared
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # add a set of axes to the figure
ax.scatter(
    x, y, s=80, alpha=0.5
)  # draw the scatter plot with labels of x and y separately with 80 by 80 points and half transparent
ax.set_xlabel("X")  # set the x-axis label
ax.set_ylabel("$y=x^2$")  # set the y-label including symbols like $ y = x ^ 2 $
ax.set_title("scatter plot with matplotlib")  # set the title
plt.show()  # show the figure

# Plotting a random scatter plot (setting marker color in RGB format)

fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # add a set of axis to the figure
N = 5  # set N=5 as number of points in each dimension
x, y = (
    np.random.random((2, N)) * 10
)  # generate x, y coordinate arrays with N data points between 0 and 9
size = (
    200 * np.random.random(N) + 100
)  # generate size array   with range of 100~300 for each point
color = np.random.random((N, 4))
ax.scatter(x, y, size, color)  # draw the scatter plot with labels of x and y separately
ax.set_xlabel("X")  # set the x-axis label
ax.set_ylabel("Y")  # set the y-label including symbols like $ y = x ^ 2 $
ax.set_title("random scatter plot with matplotlib")  # set the title
plt.show()  # show the figure

# B Bar plots
############################
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # create an axes
menMeans = [20, 35, 30, 35, 27]  # means of a male group
womenMeans = [25, 32, 34, 20, 25]  # means of a female group
menStd = [2, 3, 4, 1, 2]  # standard deviations of the male group
womenStd = [3, 5, 2, 3, 3]  # standard deviations of the female group
indx = np.arange(5)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence
rects1 = ax.bar(
    indx, menMeans, width, color="r", yerr=menStd
)  # draws male group bar plots (use error bar to show standard deviations)
rects2 = ax.bar(
    indx + width, womenMeans, width, color="y", yerr=womenStd
)  # draws female group bar plots (use error bar to show standard deviations)
ax.set_ylabel("Scores")  # set the y-axis label
ax.set_title("Scores by group and gender")  # set the title
ax.set_xticks(indx + width)  # set the x-axis ticks with range from indx+width
ax.set_xticklabels(("G1", "G2", "G3", "G4", "G5"))  # set the names of the x-axis ticks
ax.legend((rects1[0], rects2[0]), ("Men", "Women"))  # add a legend
plt.show()


def autolabel(rects):  # a function to show data values on top of bars
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            1.05 * height,
            "%d" % int(height),
            ha="center",
            va="bottom",
        )


autolabel(rects1)  # apply autolabel to the male group bars
autolabel(rects2)  # apply autolabel to the female group bars

# C Histograms
#########################
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # add a set of axis to the figure
n, bins, patches = ax.hist(
    np.random.randn(1000), 50, facecolor="r", alpha=0.75
)  # create a histogram of random numbers drawn from normal distribution
ax.set_xlabel("Smarts")  # set the x-axis label
ax.set_ylabel("Probability")  # set the y-label including symbols like $ y = x ^ 2 $
ax.set_title(
    r"$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$"
)  # set the title with some mathematical expressions
plt.show()  # show the figure

# D Drawing pie charts:
############################
# A pie chart is a circular chart divided into sectors, illustrating numerical proportion.
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111)  # add a set of axis to the figure
# prepare the data
labels = "Python", "C++", "Ruby", "Java"  # labels for each section of the pie chart
fracs = [
    35,
    22,
    17,
    18,
]  # corresponding values for each label (the scores are generated randomly)
explode = (
    0,
    0,
    0.1,
    0,
)  # set the displace length of different sections. In this example, Ruby is enlarged with displace length 0.1
# compared to the others
# draw it!
ax.pie(
    fracs,
    explode=explode,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
)  # first two parameters must be required
ax.set_title("Programming Skills")  # set the title
plt.show()  # show the figure

# E Drawing 3D plots: Here we will use 3D surface plot to draw a random surface generated by random numbers
############################################################################################################
fig = plt.figure()  # create a figure
# prepare some data points
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
c = np.random.rand(N) * 50 + 1
# draw it
ax = fig.add_subplot(111, projection="3d")  # add a set of axis to the figure
ax.scatter(
    x, y, c
)  # draw a 3D scatter plot with labels of x and y separately with size and color data separately
ax.set_xlabel("X")  # set the x-axis label
ax.set_ylabel("Y")  # set the y-label including symbols like $ y = x ^ 2 $
ax.set_zlabel("Z")  # set the y-label including symbols like $ y = x ^ 2 $
ax.set_title("3D scatter plot with matplotlib")  # set the title
plt.show()  # show the figure

# F Include two kinds of y-axis
###############################
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(1, 10, 0.2)
y = np.sin(x)
ax.plot(x, y)
ax2 = ax.twinx()
y2 = np.cos(x)
ax2.plot(x, y2, "ro-")
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax2.set_ylabel("Z label")
plt.show()

# G Using subplots
############################
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
x = np.arange(1, 10, 0.2)
y = np.sin(x)
ax1.plot(x, y)
ax2.plot(x, y)
plt.show()

