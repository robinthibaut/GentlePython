#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part introduces the numpy package and its essential uses!

import numpy as np

# numpy is a package that provides a high-performance multidimensional array object.

print("How to create a numpy array:")
print("Easiest way (by calling the numpy function)")
arr = np.array([1, 2, 3])  # Create a rank 1 array using a list
print(type(arr))  # Prints "<class 'numpy.ndarray'>"
print(arr.shape)  # Prints "(3,)"
print(arr[0], arr[1], arr[2])  # Prints "1 2 3"
print(arr[0:2])  # Works like in lists
print("")

arr = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array using lists of lists
print(arr.shape)  # Prints "(2, 3)"
print(arr[0, 0], arr[0, 1], arr[1, 0])  # Prints "1 2 4"
print("")

# Type of elements of the array can be specified:
float_arr = np.array(
    [1, 2, 3], dtype=np.float64
)  # float64 is the default type in python

# If you want to change the type of an existing array (if you can):
int_arr = np.array([1.0, 2.0, 3.0])  # The input list has floats in it!
int_arr = int_arr.astype(np.int64)  # Now it uses int64 as datatype!

# Arithmetic operations with arrays are applied element-wise:
print("Element-wise computation between arrays and single numbers: ")
x = np.array(
    [[1, 2], [3, 4]], dtype=np.float64
)  # Create a rank 2 array with floats in it!
y = np.array(
    [[5, 6], [7, 8]], dtype=np.float64
)  # Create another rank 2 array with floats in it!
# All of the following computations between arrays are element-wise!:
print(
    "Automatic element-wise computation between x and y; gives a new array with the same dimensions!"
)  # Works element wise and gives a new array back!
print(x + y)  # Elementwise sum;     [[ 6.0  8.0] [10.0 12.0]]
print(x - y)  # Elementwise difference; [[-4.0 -4.0] [-4.0 -4.0]]
print(x * y)  # Elementwise product; [[ 5. 12.] [21. 32.]]
print(x / y)  # Elementwise division; [[0.2        0.33333333] [0.42857143 0.5       ]]
print(x**y)  # Elementwise power;    [[  1.  64.] [ 2187. 8748.]]
# Other operations like +=, *=, -= and **= are also possible with numpy arrays!
print("")

print("Element-wise computation between arrays and single numbers: ")
print("Operations with single numbers: ")
x = np.array(
    [[1, 2], [3, 4]], dtype=np.float64
)  # Create a rank 2 array with floats in it!
print(x + 2)  # Elementwise sum with a number;       [[3. 4.] [5. 6.]]
print(x - 2)  # Elementwise substraction with a number; [[-1. 0.] [1. 2.]]
print(x * 2)  # Elementwise product with a number; [[2. 4.] [6. 8.]]
print(x / 2)  # Elementwise division by a number; [[0.5 1. ] [1.5 2. ]]
print(x**2)  # Elementwise exponentation by a number; [[ 1. 4.] [ 9. 16.]]

# It is also possible to apply basic linear algebra computations like the dot product of two vectors! Only these
# linear algebra functions work on numpy arrays: 'dot', 'trace', 'transpose', 'linalg.inv' and 'linalg.diag'. (matrix
# multiplication, trace of a matrix, transpose of a matrix, inverse of a square matrix and diagonal)
print("")
print("Dealing with higher dimensions: ")
x = np.array([[1, 2], [3, 4]])  # Create a rank 2 array with ints in it!
y = np.array([[5, 6], [7, 8]])  # Create another rank 2 array with ints in it!
v = np.array([9, 10])  # Create a rank 1 array with ints in it!
w = np.array([11, 12])  # Create another rank 1 array with ints in it!

# User 'dot' to compute the inner product of two vectors (they must have the same number of elements):
print("The dot product of two vectors: (result is a number) ")
print(v.dot(w))  # Prints 219
print("")
print(
    "The dot product of two arrays; works just like the multiplication of matrices: "
)  # Works element-wise on the two arrays and gives an array back!
print(x.dot(v))  # Prints [29 67]
print("")
print(
    "Using transpose function 'T' on x to compute the matrix product of x and y: "
)  # Works element-wise on the two arrays and gives an array back!
print(x.dot(y))  # Prints [[19 22] [43 50]]
# The transpose function 'T' is used to transpose an array:
print("")
print("Using T on x to transpose it: ")  # Gives you a new array back!
print(x.T)  # Prints [[1 3] [2 4]]
# The linalg.inv function is used to invert a square matrix:
print("")
print("Using linalg.inv on x to invert it: ")  # Gives you a new array back!
print(np.linalg.inv(x))  # Prints [[-2.   1. ] [1.5 -0.5]]
# The linalg.diag function is used to extract the diagonals of an array:
y = np.array([[5, 6], [7, 8]])  # Create another rank 2 array with ints in it!
print("")
print(
    "Using linalg.diag on y to extract the diagonals of it: "
)  # Gives you a new array back!
print(np.linalg.diag(y))  # Prints [5 8]
