#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners This is a tutorial of the Python Programming Language. It begins by taking
# you all the way from basic console commands and data types all the way to Object Oriented Programming in Python.
# I hope you enjoy it!

import copy  # copy is  a module that allows you to copy objects. It comes with the standard library, but needs to
# be imported. We will use it later in this tutorial.

# In order to run selected lines, you can use the Pycharm shortcut.

# Part #1 : Introduction And Overview

print("Hello World")  # Prints "Hello World" to the console.
# The console can be viewed by hitting the console tab in the bottom left-hand side of the PyCharm window.

# Part #2 : Variables And Data Types
my_var = "Hello"  # This is a string variable, a string is a collection of characters.
my_char = "c"  # This is a character.
my_int = 12  # Integers are whole numbers, whereas floats are decimals.
my_float = 19.99  # This is a floating point number (decimal).
my_bool = True  # Boolean Values are True or False, these are usually used for condition checking.

# Part #3 : Math Operators
print("5 + 2 =", 5 + 2)  # Addition (+) prints "5 + 2 = 7"
print("5 - 2 =", 5 - 2)  # Subtraction (-) prints "5 - 2 = 3"
print("5 * 2 =", 5 * 2)  # Multiplication (*) prints "5 * 2 = 10"
print(
    "5 / 2 =", 5 / 2
)  # Division (/) prints "5 / 2 = 2.5" this is because one of the values being divided is a float value, meaning it
# is treated as a float!
print(
    "5 // 2 =", 5 // 2
)  # Floor Division (//) is similar to division, but it removes the remainder and rounds down to the nearest whole
# number. Prints "5 // 2 = 2"
print(
    "5 ** 2 =", 5**2
)  # Exponent (**) Prints "5 ** 2 = 25"   5 squared in this case!
print(
    "1 + 6 * 3 =", 1 + 6 * 3
)  # Operator Precedence dictates the order of execution of operations. PEDMAS applies to Python, as it does to all
# maths. Parentheses: (), Exponents: **, Multiplication or Division (from left to right), Addition or Subtraction
# from left to right. In the example above Multiplication will be done first because (*) has higher precedence than (
# +). Prints "1 + 6 * 3 = 19"


# Part #4 : Type Conversion And Casting
# Casting is the process of changing the type of data.
x = int(
    1
)  # x will be 1 and print out 1 because int(1) converts 1 to an integer value of 1.
y = int(
    7.0
)  # y will be 7 and print out 7 because python removes any decimals on floats to make them integers. Integers can be
# converted to floats however! We can convert ints to floats using float(1), this would make 1 a float value such as
# 1.0. More on that later!
z = float(
    "1"
)  # z will be 1 and print out 1 because there are many ways we can go about converting strings to float values,
# one of which being in the form float("1") where "1" contains the characters "1". These characters will be cast and a
# float value of 1 will result from it!
n = float(
    "nan"
)  # n will be nan, standing for not a number and when printed will also say not a number due to the fact that this
# value does not exist in maths land! Woah! Magic Python!

# Part #5 : User Input
name = input(
    "What is your name?"
)  # Let's use this cool 'input' built-in method to take some input from the user!
print(
    "Hello", name, "nice to meet you!"
)  # This is used by typing input() and in the parameters we type a string value
age = input(
    "Enter your age: "
)  # containing the question we would like answered by the user! The first line of code above asks what is your name?
# age = "Enter your age:"

# Part #6 : String Manipulation + User Input
age = int(
    input("Enter your age: ")
)  # This line is pretty much the same as line 42, however we are taking advantage of type casting here to convert
# the input from a string to an integer using the int() built-in method! This means we can do maths with it later on!
dog_years = (
    age * 7
)  # note that we are not printing the value of age here! We are just assigning it to a new variable dog_years,
# which contains the equation which converts human years to dog years! (1 human year = 7 dog years)
print(
    age, "human years is equal to", dog_years, "dog years!"
)  # Next we can print out both our human years and our dog years on separate lines:

# Part #7 : While Loop And Increment Operator
i = 1  # Initialize i with a value of 1 so that it may enter our loop
while (
    i <= 5
):  # Create a while loop where expression (i<= 5) is true. Will execute as long as expression is true. { Below shows
    # what i will equal after each loop iteration }
    print(
        "*" * i
    )  # 5 iterations means print '*' 5 times where each * is on a new line as print by default prints things on
    # different lines during each invocation or call. Print Multiply '*' by i and return result. This will always
    # execute first and then loop back around! Below shows what i will equal after each loop iteration:
    i = (
        i + 1
    )  # Loop Iteration 1: i will equal 2 because we are incrementing it by 1 via i+=1; Loop Iteration 2: i will
    # equal 3 because we are incrementing it by 1 via i+=1; Loop Iteration 3: i will equal 4 because we are
    # incrementing it by 1 via i+=1; And so on... Until while loop expression becomes false and loop terminates!

    # Note that you need a space between the asterisk symbol and what you want to appear after, else no space appears: (
    # i.e. - print('*'*i) = print('*****') whereas print('* '*i) = print('* * * * * ')). When printing 5 asterisks in
    # this manner, if there is no space between them, they all stick together like so: '*****' vs '* * * * *'.

# Part #8 : For Loop And Range Function + Increment Operator
for i in range(1, 6):
    print(i)
# range allows us to define where our for loop starts (1) and where it ends (6 can be thought of as
# NumberOfIterations at which point loop will terminate), initializing i to 1 before starting loop then increasing
# its value by 1 until numberOfIterations == 6. Whole numbers only for range function! Starting with 0 instead of 1
# does not change results because python starts counting at 0 for lists so either way we get 0-5. The result is also
# identical had we just done range(6): The code would have still started at 0 then gone up by one where its final
# value would be 5 after executing 6 times! Note that it always starts at 0 when doing range(n). The last number
# given must be n+1 to get n number of iterations starting at 0! It always goes up in intervals of 1 UNLESS an
# additional argument 3rd argument is specified (range(0,11,2)) goes up by 2's instead of 1's!). Look up range
# function if you are unfamiliar with it! The final number of iterations depends on how many numbers are counted
# starting from startingNumber TO endingNumber WHERE endingNumber < finalNumberOfIterations otherwise we would get a
# blank line because there would never be another iteration! Example Range(2 to 10 counts 8 numbers!) 2 3 4 5 6 7 8 9
# 10  |Range(2 to 11 counts 9 numbers!) 2 3 4 5 6 7 8 9 10 11 |Range(3 to 12 counts 9 numbers!) 3 4 5 6 7 8 9 10 11
# 12|Range(4 to 13 counts 9 numbers!) 4 5 6 7 8 9 10 11 12 13|Range(0 to 10 counts 10Numbers!) 0 1 2 3 4 5 6 7 8 9 10
# | Note that range STILL starts counting at 0 even though we specified a start value of 2 and an end value of 10
# instead of saying numberOfIterations and endingValue respectively! Once loop terminates its final value
# incrementally increases according to how many iterations there have been already!:LoopI0 + EndValueRemains0LoopI1 +
# EndValueRemains1LoopI2 + EndValueRemains2LoopI3 + EndValueRemains3LoopI4 + EndValueRemains4LoopI5 +
# EndValueRemains5 etc...Just remember that python starts counting at zero for lists so either way you would get
# 0-5! Try different values for yourself such as range(1,9), range(0,11), range(10). You should always get 9 values
# returned instead of 8 just remember your ending value must always be n+1! The goal here is to understand why the
# final result of printing this out should contain 9 values not just 8 no matter how many times or which way I run my
# loop even though I only specified an end value of 8 for numberOfIterations!: 4,2,3,4,2, 3,4,2,3. (Note how we are
# missing the number 1 and not 8 because range() function starts counting at 0). This same example can be written in
# a for loop in the form for i in range(1,9) and will produce the same result when printing.

for i in range(
    4
):  # This is the same for loop as above but with a different integer value! This loop starts at 0 instead of 1 and
    # ends at numberOfIterations -1 (for 4 iterations we would do range(0,5) where 5 is numberOfIterations+1 and
    # would result in 0-4 being returned instead of 1-5 as we have done above!
    print(
        i
    )  # Print all values in order of iteration! Range function is really useful and again make sure you look it up
    # if you are not 100% comfortable with it! It will come up in an interview!

fruits = [
    "Apples",
    "Bananas",
    "Grapes",
    "Oranges",
    "Pineapple",
]  # Create a list called fruits which will hold all our fruit names! List indices start at 0! Lists can hold any
# data type! Strings can also be indexed like a list! Create your own list of some sort then print its elements out
# to make sure you fully understand how this works! Always check your final values in lists by printing out data from
# index positions! Lists are literally just variables which hold a group of other variables where these other
# variables hold their respective values! In the case of my example above each element is of data type string! Try
# creating your own lists!

for fruit in fruits:
    # The for loop above called for i in range(4), now we will change i to the word fruit in order to replace fruit
    # with Apples, then Bananas then Grapes until last value which is Pineapple where it stops because it reached end
    # value or numberOfIterations! This is another cool built-in method which we can also use to iterate through
    # every element in our 'fruits' list. We can just do one more example where we create our own list full of
    # numbers and integers! See how far you get!
    print(fruit)
    # Try creating your own lists of numbers or (Works for strings too) letters then print elements out to
    # determine what sort of data type their respective values are.

# Part #9 : If Statement And Comparison Operators
if (
    13 < 20
):  # if statement checks condition given against some kind of truth value. If condition is True it proceeds to
    # execute first line of code then continues to execute code after until completed.
    print(
        "13 < 20"
    )  # A condition can be created using one or more comparison operator: < : Less Than, > : Greater Than,
    # <= : Less Than Or Equal To , >= : Greater Than Or Equal To  Which are all self explanatory. == : Equal To (Two
    # Equal Signs Because One Is Already Used For Assignment Operator) != : Not Equal To These comparison operators
    # can be used on both numbers and strings where they can be used to check for equality, their result will always
    # be a Boolean type (True or False). We can also use compound statements such as "and" and "or" which can use
    # more than one condition in order to come to a conclusion. One of the most important things to take away from
    # this is that you must write your if statement with a colon at the ending and indent each line of code with 4
    # spaces or a tab in order to execute it properly! Everything after this colon is considered by Python to be
    # part of our if-block or if statement's suite of statements (indentation is important here) In short this line:
    # if 13<20: means that if our condition is true then proceed to execute code in if-block.
    print(
        "condition"
    )  # We will briefly cover nested-blocks as well, for now know that these simply exist inside another block of
    # code this will make more sense after we cover functions and variable scope.

# Part #10 : If Else Statement + Comparison Operators And Logical Operators
x = 5
y = 8
z = 5

if (
    z < y > x
):  # Here we have a compound comparison operator. This means we are combining more than one comparison operator( z <
    # y > x). Here we are saying execute if z(5) is less than y(8) AND y(8) is greater than x(5). If our compound
    # statement evaluates to true then execute code in conditional block. Notice how we need to use 2 comparison
    # operators as it says both y and x must be greater in order to execute code!:
    print("y is greater than z and y is greater than x")

if (
    z <= x
):  # An Else Statement Can Be Used To Execute Code If Condition Fails! You Must Indent Each Line Like The If
    # Statement! Example:
    print(
        "z is less than or equal to x"
    )  # Statements here will only run if condition given above evaluates to True otherwise program will not run this
    # else block!
else:  # If condition/expression does not hold true, then else will be executed instead where it can serve as a
    # fallback function for when our first condition fails.
    print(
        "x is greater than z"
    )  # Statements here will only be executed if the original condition does not hold!

age = int(
    input("Enter Age: ")
)  # Note that this only works when one condition must hold true. In cases where we want an input value to be equal
# to one value or another then we would have to use an 'if elif else' (if-else-if). Copy+Paste the following lines
# between lines 58-61 in the PyCharm IDLE Editor and make sure notes are read before executing for understanding!:

if (
    age >= 5 and age <= 10
):  # This if statement checks whether age is greater than or equal to 5 AND less than or equal to 10 using a logical
    # operator "and". Which means both conditions must hold true in this case!, It Has Been Met We Can Now Execute
    # The Code In The Following Block
    print("Go To Primary School")

elif (
    age >= 11 and age <= 18
):  # Allows us to chain another statement after our initial if block, checking whether the value of age is greater
    # than or equal to 11 AND less than or equal to 18 using the "and" logical operator. Notice how we can use
    # nested-blocks here by executing the code here only if THIS condition holds true! If it does, we can then
    # execute code in this block!
    print("Go To Secondary School")

else:  # If no other condition holds true we can simply print out this message because it will not make sense for a
    # person under the age of 5 to attend school in this context.
    print("Go To Tertiary School")

# Part #11 : List, Tuples and Sets
fruits = [
    "Apples",
    "Oranges",
    "Bananas",
]  # This will create a list variable that contains 3 string values. Lists can hold many different types of data and
# can be indexed in the same way strings are! It is important to note the difference between mutable and immutable
# variables. Mutable variables are ones which can be changed in place whilst immutable variables cannot be.
# Appending, removing and changing values in lists is perfectly fine to do on the spot as they are considered
# mutable. Strings and Tuple or two examples of immutable data types. You can not change values stored in strings or
# tuples by indexing them instead must create a brand-new variable. Let's talk about tuples now!
fruits = (
    "Apples",
    "Oranges",
    "Bananas",
    "Grapes",
)  # This will create a tuple variable that contains 4 string values. Tuples are also lists except they are
# surrounded by parenthesis instead of brackets, their variety in which they store data is also less. Tuples values
# can not be changed however they can be removed, or added to entirely- new variant called concatenation is used to
# accomplish this however this is much slower than standard appending operations offered by lists so one should
# consider using lists over tuples unless you have some good reason not to! Tuples use less memory than lists and
# are very relevant in situations such as sequences with an undefined length (such as a file's contents). Tuples like
# lists also start with an index value of 0 and can be indexed just like both strings and lists! If you assign a
# tuple to a variable you can use multiple assignment technique! Multiple assignment means that you can assign one
# variable to more than one value! An example of this could be x,y = 1,2 . Here x is set to 1 and y is set to 2 .
# The comma acts as a glue for assigning multiple values via single line of code. Sets are another data structure you
# should know about, try creating your own set then print out all it's elements to get an understanding of what it
# does. In summary sets act like an unordered list but cannot contain duplicate values! After creating your own set
# print out its elements using methods such as print(yourSetVariableName) and then go ahead and start looking up how
# to perform many different operations and methods using it such as intersection, union, etc and try writing your own
# code using these! Remember that sets contain unique values and values inside them cannot be indexed otherwise we
# would end up with duplicate ones! The sooner you learn about these built-in data structures, the sooner you will
# become comfortable with them! To finish off, remember that when storing data it is important to not only store
# what you need but also to store it correctly! Use lists or tuples when you know exactly what data you need but
# don't care about ordering, use sets when you care about having duplicate free collections but don't need indexing!
no_duplicates = set(
    {}
)  # We create a new set which is surrounded by curly brackets {}, however this time our set is empty because we have
# nothing inside the curly braces. We could simply have done no_duplicates = {} but then we would end up with an
# empty dictionary instead so make sure you get familiar with these structures quickly!
# Part #11 : Dictionaries
account = {
    "username": "python",
    "password": "123",
    "balance": 100.0,
}  # This will create a dictionary variable that contains 3 keys and 3 values. Dictionary's are a special type of
# data structure because they do not use indices at all and instead make use of keys which are linked to values!
# Keys can be of any immutable data type such as numbers or strings. Values can be of any data type, including lists
# and dictionaries! We call dictionaries "mappings" because they "map" or "associate" keys to values! The general
# syntax for creating dictionaries is: someDictionaryVariableName = {key1: value1, key2: value2, etc}. We can get
# values from dictionaries by simply indexing them! To index them we assign our dictionary variable to a key in the
# form of someDictionaryVariableName[key], this will return the value associated with the key we supplied. If the key
# does not exist then it will throw a key error! To check if a key exists in the dictionary we write
# someDictionaryVariableName.get(key) , this will return None if the key does not exist, otherwise it will return the
# value! It is important to note that dictionaries always have unique keys but can have duplicate values! Accessing
# items using get is much faster than using [key] ! Use get if you are trying to print out input that requires a key
# but you do not know whether it exists in your dictionary or not (we will cover exceptions and error handling
# soon!). Now let's look at some operations we can perform with our newly made accounts dictionary:
print(account["username"])  # This will print out python
account["username"] = "johndoe"  # This will change the username from python to johndoe!
print(
    account["username"]
)  # This will print out johndoe now that we overwrote our original key's value!
account[
    "balance"
] += 50  # This will increment our balance by 50 (add 50 to it) ! Resulting in account['balance'] being equal to 150
# as it is now!
del account[
    "password"
]  # This will remove our password key from accounts dictionary! Remember we can only delete things by their keys!
print(
    account
)  # EXPLAIN THIS PRINT OUT! Answers: Our new dictionary should look like this: {'username': 'johndoe', 'balance':
# 150}. Index keys in dictionaries cannot be unassigned like the way list elements can, if you want to delete
# something from a dictionary then you must use del (delete) built-in method! We can also do add new keys and values
# to our dictionary using this form: someDictionaryVariableName[key] = value . Sometimes however we might have
# situations where we store empty dictionaries, or dictionaries which were copied off of other real ones! Let's say
# that all our accounts dictionaries are copies of account, how would we fill them with separate values and not
# overwrite each other!?. Well one way we could do this is by declaring an empty dictionary and then filling it with
# different sets of data afterwards. In order to do this let's create some empty dictionaries, fill one and see what
# happens:
empty_dict1 = {}  # We create an empty dictionary
empty_dict2 = {}  # We create another empty dictionary
empty_dict1["username"] = "johndoe"  # We add a new key and value pair to our first dictionary!
print(
    empty_dict2
)  # We print out empty_dict2 to determine whether inserting data into a different dictionary affects another
# that has the same structure as the first! Answer: {}, no it does not! We could also do things like make copies of
# dictionaries using the built-in copy() method:
empty_dict3 = copy.copy(
    account
)  # We create a new dictionary empty_dict3 and this time we make it a copy of our original accounts dictionary. When
# we print out its contents to verify this has worked we will be presented with a copy of our account dictionary!
# Note that when you use something like empty_copy = account, only the reference to the original account variable is
# copied, not the contained values! When we print you should see {'username': 'johndoe', 'balance': 150}

# Part #12 : Mutable Versus Immutable Types
myint = 10  # Integers are immutable meaning that once created we can not change the contained value in place but we
# can overwrite it entirely. (We will look at overwriting another time). Take note of how if i try to change the
# value of myint in memory to '20' then i will get a TypeError saying that i can't do that because myint is
# immutable! Attempting to change values in immutable data structures usually result in errors and you will get very
# familiar with them soon enough! The same goes for strings, strings are also immutable meaning you cant change their
# contained values either! Try creating your own integer variable and string variable and see what happens when you
# attempt to modify them!
print(myint)  # This will print out 10 because it was originally 10
myint = 20  # This will overwrite value of myint stored in memory space (will not modify it in place) but instead
# create new myint variable and leave old one to garbage collection. Old space will be overwritten with new myint
# value this time being 20!
print(
    myint
)  # This will now print out 20! Because myint got overwritten but never modified in place! The same goes for
# strings! Here is an example with strings: Here is an example with strings: Strings are actually sequences which
# means that if given an index in astring[0] we will get whatever character is located at index 0 within our string,
# if such an index does not exist then python throws an error telling us of this. This means however that we can play
# around with strings and slice them, split them or even join them together! In order to join two strings together
# we use something called concatenation. Concatenation is when we add one string to another like so:
# someStringVariableName + "SomeOtherString". This works because "+" is overloaded and here means concatenation!
# Concatenation always creates a new string, it does not modify either of it's parameters in place! So be careful
# when performing operations on strings! Last but not least lets talk about lists since these are mutable and we can
# modify the contained values in them if we so choose!
mylist = [1, 2, 3, 4]  # Create new list with values 1-4
print(mylist)  # Print out values in mylist, which will be (1,2,3,4)
mylist[
    -1
] = 5  # Change last value in list from 4 to 5 using square bracket indexing of list (using negative numbers means we
# start from the end)!
print(
    mylist
)  # Print out values in mylist again this time it will be (1,2,3,5) because we modified the last value in the list!
mylist.append(7)  # Use append built-in method to append new value 7 at end of list!
print(
    mylist
)  # Should print out (1,2,3,5,7) now because we appended 7 to our original list!

# Part #13 : Comments And DocStrings
# print(13 + 9 + 11 + 14 + 12 + 9 + 9 + 5 + 9 + 8 + 7 + 5 + 6 + 6 + 9)
# This is a single line comment which ignores everything after the hash symbol until it hits a newline (line
# break)! This can also be done inside loops or functions! This is another example of a single line comment! These
# are useful for leaving notes for yourself when other people who read your code don't always know what you mean! It
# also helps keep track of what you have done with code and what you want to do next! Code without comments is
# always messy and unorganized! Docstrings however are useful for both you and people who read your code!
# Docstrings are used to describe a function's purpose or method's functionality for example. You can get your
# docstring back by simply calling yourFunctionName.__doc__ . Try entering the following lines of code into PyCharm
# and see what happens:

""" This is a multiline/block comment, it's similar to single line comments except they span multiple contiguous lines 
instead of just one! They are done by placing three single or double quotes in front of the actual comment and then 
again after it has been written. These can also be placed inside loops, functions or outside of them if you so 
please but will still have the desired effect! """
# This will print nothing to the console but if you hover over it
# then look at its tooltip then you will see it is there! You can also right-click on it and select view docstring
# to open up a window containing this text! Note that comments and docstrings are strip out by python when it
# executes so don't worry about taking up memory space when writing code! Also know that execution happens from top
# down so even if this was placed on top empty line it would still be executed first as long as nothing precedes it!
# You should be aware that some programming languages ignore single line comments entirely but this does not apply to
# python so make sure you get used to using them! Copy+paste the following lines into PyCharm underneath your
# preceding lines 53-70:


def message():  # Declare function message() which does not take any parameters.
    """Prints a message to the console"""  # This is our function's doc string, the reason it is triple quoted is
    # because it is a more than one line!
    print("Hello World!")  # Print message "Hello World!" to console!


message()  # Invoke our function!
print(message.__doc__)  # Print our function's docstring to console!


# Part #14 : Functions
def myfunc(
    n,
):  # Define function that takes single parameter. When we call a function we pass arguments via parameters. In the
    # example below our argument is 'n' and the value that is passed in to the function (i.e. myfunc(5)) will be
    # assigned to 'n'. In this case 5 will be assigned to n inside the function body. If we forget to pass in an
    # argument when calling a function then we get what we call a TypeError! Copy+paste this code in PyCharm
    # underneath your preceding lines 75-85! Note that when declaring functions, you must always include a colon (:)
    # at the end! Remember when using def keyword to define functions: def someFunctionName():
    if (
        n % 2 == 0
    ):  # We create an if statement to check if remainder of n/2 is equal to 0, % means modulus or remainder and ==
        # means equal to operator and 0 means 0! Later on we will also cover relative comparisons such as greater
        # than or lesser than comparisons (== means equal to!).
        print(
            n, "is even"
        )  # Print value of n and string "is even" if condition returns True , this code will be executed first
        # inside our new myfunc body! See how it works below! Next we create an else clause which if our statements
        # condition checks return false will execute the print statement instead! See how it works below! Be sure to
        # note the indentations with 4 spaces per line!

    else:
        print(
            n, "is odd"
        )  # Print value of n and string "is odd" else print statement inside else clause!


myfunc(
    5
)  # Invoke out myfunc() and pass in argument 5 via parameter n!, n's value will now be equal to 5 at this point in
# time inside our function body! We can also just do something like replace "if-else" statement with another print
# statement that returned something like: "Please enter an integer.", that would work as well but for now just run
# your code so far and make sure it works before continuing on with tutorial! If you are getting syntax errors then
# you may have forgotten to add the colons on some lines or indented improperly or did not include something we
# covered previously!
