#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part contains exercises to familiarize yourself with Python

# Exercise 1
# Find a way to swap the values of x and y
# Make sure to uncomment the print statement before running this file!
x = 5
y = 10


# print(x, y)

# Exercise 2
# Move the part that creates node3 before the declaration of node2
# print node3.val before and after running this file to see the change in value!
class Node:
    def __init__(self, value):
        self.val = value


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
print(node3.val)

# Exercise 3
# Print the value of list2 after running this file!
list1 = [1, 2, 3]
list2 = list1
list1[0] = 0
# print


# Exercise 4
# Print the average of all the values of x for each index location! Remember that this is a list of lists!
arr = [[1, 2], [3, 4], [5, 6], [7, 8]]
# print


# Exercise 5 You can check if the item exists in python dictionaries using the function "get"! Uncomment the print
# statements to see the difference!
student = {"name": "John", "age": 30, "courses": ["Math", "CompSci"]}
# print (student.get("Age", -1))
# print (student.get("name", -1))


# Exercise 6
# Slicing is the act of extracting a portion of the list! Uncomment the print statements to execute!
ourlist = [1, 2, 3, 4, 5]
# print (ourlist[2:])
# print (ourlist[:3])


# Exercise 7 Tuples are immutable lists. You cannot change their values once they are assigned. Change tuple1 to
# tuple2 and see what happens when you uncomment it!
tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)
tuple3 = tuple([1, 2])
tuple4 = tuple("Hello")

print(tuple1 == tuple2)  # Do these two tuples have the same values? True or False?


# Exercise 8
# You can use the function "sorted" to sort a list in ascending order! Uncomment the print statements to execute!
mylist = [5, 2, 3, 1, 4]
# print (sorted(mylist))
# print (mylist)


# Exercise 9
# Practice making a dictionary using the dictionary comprehension feature in python!
numbers = range(10)
dictionary = {x: x ** 2 for x in numbers}


# Exercise 10
# Dictionaries can also be made using the zip function! Uncomment to execute!
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
zipped_dict = dict(zip(dict1.values(), dict2.values()))


# Exercise 11
# You can also iterate through dictionaries using a for loop!
our_dict = {"a": 1, "b": 2, "c": 3}


# Exercise 12
# Let's practice making 2D lists! Make the board, and then change the center square to the value 2!
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
# print (board)

# Exercise 13
# Let's implement a function that finds the minimum value of our 2D list, board!
# 1. Define a function called min_value that takes in a list, and returns the minimum value of all the elements in the
# list!
# 2. Then, use the min_value function to find the minimum value in board!
# Hint: You can use min_value inside of min_value!
board = [[2, 0], [1, 0]]
# print (min_value(board))


# Exercise 14
# You can zip with multiple lists! Uncomment the print statements!
nums1 = (1, 2, 3)
nums2 = (4, 5, 6)
nums3 = (7, 8, 9)
# print (list(zip(nums1, nums2, nums3)))
# print (list(zip(*zip(nums1, nums2, nums3))))

# Exercise 15
# There is a string method called count that counts the amount of times a given substring of a string is present!
# Uncomment the print statements!
message = "Hello, world!"
# print (message.count("ello"))

# Exercise 16
# The partition function splits a string into two substrings at the first occurence of a given string within the parent
# string!
# print (message.partition("ello"))

# Exercise 17
# You can check if a string contains another string using the method "find"
# Uncomment the if statements and observe the output generated!
message = "Hello, world!"
# print (message.find("Hello"))
# print (message.find("Hello, world!"))
# print (message.find("Hello, World!"))

# Exercise 18
# Use the function "isupper" to check if the given string contains upper case characters
message = "Hello, world!"
# print (message.isupper())

# Exercise 19
# You can check if the string is title case using the method "istitle"
message = "Hello, world!"
# print (message.istitle())

# Exercise 20
# You can iterate through the characters of a string using the method "enumerate"
message = "Hello, world!"
# print (enumerate(message))
# for i, item in enumerate(message):
#     print (i, item)

# Exercise 21
# What will be printed out? Uncomment to execute!
t = (1, 2, 3)
# print (t.index(1))
# print (t.index(0))

# Exercise 22
# You can make sets with the set keyword! Uncomment to execute!
s = {1, 2, 3}
# print (1 in s)
# print (0 in s)

# Exercise 23
# You can make sets out of lists! Uncomment to execute!
ourlist = [1, 2, 3]
# s = set(ourlist)

# Exercise 24
# You can convert a set back to a list using the list keyword! Uncomment to execute!
s = {1, 2, 3}
# print (list(s))

# Exercise 25
# You can add elements to a set using the add method! Uncomment to execute!
s = {1, 2, 3}
# s.add(4)
# print (s)
# s.add(1)
# print (s)

# Exercise 26
# You can remove elements from a set using the remove method! Uncomment to execute!
s = {1, 2, 3}
# s.remove(2)
# print (s)
# s.remove(5)


# Exercise 27
# You can clear all the elements from a set using the clear method! Uncomment to execute!
s = {1, 2, 3}
# s.clear()
# print (s)

# Exercise 28
# You can also perform operations on sets! Uncomment to execute!
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# print (s1 | s2)
# print (s1 & s2)
# print (s1 - s2)

# Exercise 29
# You can convert a dictionary to a set using the set keyword! Uncomment to execute!
dict1 = {"name": "John", "age": 30}
# s = set(dict1)
# print (s)

# Exercise 30
# You can make a frozenset with the frozenset keyword! Uncomment to execute!
s = frozenset([1, 2, 3])
print(s)

# Exercise 31
# Uncomment the print statements below to execute!
# print (all([1>0, 1==1, 1<2]))
# print (all([1<0, 1==1, 1<2]))
# print (all([1>0, 1!=1, 1<2]))

# Exercise 32
# Uncomment the print statements below to execute!
# print (any([1<0, 1==1, 1<2]))
# print (any([1<0, 1!=1, 1<2]))
# print (any([1<0, 1!=1, 1>2]))

# Exercise 33
# Uncomment the print statements below to execute!
# print (ascii(1))
# print (ascii('Hello'))
# print (ascii(True))
# print (ascii(1.0))
# print (ascii(1+2j))

# Exercise 34
# Passing a list as an argument! Uncomment to execute!
ourlist = [1, 2, 3]


# Exercise 35
# You can also pass multiple lists! Uncomment to execute!
# ourlist1 = [1, 2, 3]
# ourlist2 = [4, 5, 6]

# Exercise 36
# You can also pass *args with a single list or with multiple lists! Uncomment to execute!
ourlist = [1, 2, 3]
# def do_something(*args):
#     for arg in args:
#         print (arg)
# do_something(ourlist)

# Exercise 37
# You can also pass **kwargs! Uncomment to execute!
# def do_something(**kwargs):
#     print (kwargs)
# do_something(ourarg=1)
# do_something(ourarg=1, yourarg=2)

# Exercise 38
# You can also return multiple values using unpacking! Uncomment to execute!
# def return_multiple_values():
#     return 1, 2, 3
# a, b, c = return_multiple_values()

# Exercise 39
# You can also use a function within a function! Uncomment to execute!
# def return_sum(list1):
#     def do_sum():
#         sum = 0
#         for element in list1:
#             sum += element
#         return sum
#     return do_sum()
# ourlist = [1, 2, 3]
# print (return_sum(ourlist))

# Exercise 40
# You can also reuse the function within the function! Uncomment to execute!
# def return_sum(list1):
#     def do_sum():
#         sum = 0
#         for element in list1:
#             sum += element
#         return sum
#     return do_sum
# ourlist = [1, 2, 3]
# opt_list = return_sum(ourlist)
# print (opt_list)
# print (opt_list())

# Exercise 41
# You can also return functions within a function!
# def return_sum(list1):
#     def do_sum():
#         sum = 0
#         for element in list1:
#             sum += element
#         return sum
#     return do_sum
# ourlist = [1, 2, 3]
# opt_list = return_sum(ourlist)
# another_list = [4, 5, 6]
# another_sum = return_sum(another_list)

# print (opt_list)
# print (opt_list())
# print (another_sum)
# print (another_sum())

# Exercise 42
# You can also create an empty class! Uncomment to execute!
# class Person:
#     pass
# p = Person()
# p.name = "John"
# p.age = 30
# print (p.name)

# Exercise 43
# You can also create a class with the values already set! Uncomment to execute!
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("John", 30)
# print (p.name)
# print (p.age)

# Exercise 44
# You can also create a class with multiple initialization arguments! Uncomment to execute!
# class Person:
#     def __init__(self, name, age, courses):
#         self.name = name
#         self.age = age
#         self.courses = courses
# p = Person("John", 30, ["Math", "CompSci"])
# print (p.name)
# print (p.age)
# print (p.courses)

# Exercise 45
# You can also pass **kwargs! Uncomment to execute!
# def do_something(*args, **kwargs):
#     print (args)
#     print (kwargs)
# do_something(1, 2, 3, a=1, b=2, c=3)

# Exercise 46
# You can also convert a dictionary back to a list using the items method! Uncomment to execute!
# dict1 = {"name": "John", "age": 30, "courses": ["Math", "CompSci"]}
# print (list(dict1.items()))

# Exercise 47
# You can use dictionaries as keyword arguments! Uncomment to execute!
# def do_something(**kwargs):
#     print (kwargs)
# do_something(**dict1)

# Exercise 48
# You can also define a dictionary within a dictionary! Uncomment to execute!
# dict1 = {"name": "John", "age": 30, "courses": ["Math", "CompSci"], "additional_info": {"height": 6.1, "weight": 180}}
# print (dict1["additional_info"]["height"])
# print (dict1["additional_info"]["weight"])

# Exercise 49
# You can also use the list comprehension feature within a dictionary! Uncomment to execute!
numbers = range(10)
dictionary = {"num_" + str(x): x ** 2 for x in numbers}
print(dictionary)

# Exercise 50
# You can also double ** in order to unpack multiple dictionaries! Uncomment to execute!
def do_something(**kwargs):
    print(kwargs)


dict1 = {"name": "John", "age": 30}
dict2 = {"height": 6.1, "weight": 180}
# do_something(**dict1, **dict2)