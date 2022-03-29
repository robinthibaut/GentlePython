#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part explains how to deal with external data files in Python.
# For example: txt files, csv files, JSON files, Excel files.
########################################################################

# Read From File:
##################
# Read the entire file:
my_file = open(
    "some_file.txt"
)  # if file is not in current directory use the absolute path (C:\\..\\some_file.txt)
my_file.read()  # prints all the contents of the file (without skipping lines)
my_file.seek(0)  # resets the cursor to first byte of the file (default = 0)
my_file.readlines()  # reads each line as a string and puts them into a list (can be used with seek())
my_file.close()  # closes the file from memory


def read_lines(num_lines, file):
    my_line = open(file)
    for i in range(num_lines):  # includes 0 and num_lines - 1 line (byte = 0)
        print(
            my_line.readline()
        )  # line prints even if not in for loop (but for loop is faster)


read_lines(1, "some_file.txt")

# Write To Files:
##################
# Write to an existing file:
my_new_file = open(
    "some_file.txt", "w+"
)  # + can either be used when reading or writing
my_new_file.write("Some Text Here")

# File Modes In Python:
""" This argument is optional and the default value of it is "r" i.e read mode  """

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition to modes for reading/writing we also have modes for working with text and binary files:

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g images)

# How to use modes in a single string:

# r+ read and write ("r+b") means that we want to read and write in binary mode

# w+ read and write ("w+t") means that we want to read and write in text mode (the default mode)

# Two most commonly used modes: Read("r") and Read & Write("w"). They are effectively opposites of each other

# Open the file for reading
with open(
    "some_file.txt", "r"
) as file:  # [with] allows us to use the open file without having to close it
    # Using a [with] statement takes care of closing the file as well
    read_data = file.read()

# Open the file for writing (default to overwrite)
with open(
    "some_file.txt", "w"
) as file:  # [with] allows us to use the open file without having to close it
    # Using a [with] statement takes care of closing the file as well
    file.write("Hello world!")
