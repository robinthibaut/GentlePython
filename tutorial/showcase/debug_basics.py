#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part teaches how to debug a simple function using Pycharm
# I hope you enjoy it!

# debugging is the process of finding and fixing errors in a program.

import time


def display_welcome_message():
    print(f"Hello World!")


# A simple function with a bug (a division by zero)
def division(
    dividend, divider
):  # Bug in this function, divider should be a float instead of an integer
    return float(dividend) / divider


def display_result():
    dividend = input("Please enter a number to be divided, ")

    while True:
        try:
            raw_int = int(
                input("Please enter a number to divide into the first number, ")
            )  # Bug in this line, input should be a string because int() can throw a ValueError exception.

            divider = raw_int  # Bug in this line, raw_int is an integer in this case which will throw an exception
            # from the division() function, so we need to use float() to convert it to a floating point number.

            result = division(dividend, divider)

            print(f"The result is {result}")

            break

        except (
            ValueError,
            ZeroDivisionError,
        ):  # Bug in this line and true part below, this except clause will only catch the ValueError exception and
            # not the ZeroDivisionError exception thrown by the division() function if raw_int was zero. So we need
            # to change it to except (ValueError, ZeroDivisionError), and move the code dividing dividend by zero
            # into the finally clause which will always be executed at the end of the try clause even how the try
            # clause ends - like below. While we are at it, let's add a finally clause inside the while loop where
            # the try clause is used
            print()  # just to demonstrate how else and finally clauses work together. In practice you would most
            # likely have only one try or except clause inside main code.
            print("> > > " * 10)

            print("Invalid Value or Division by Zero!")

        else:  # Bug in this line, else means "if no exceptions have been raised", which is not true for this
            # function since raw_int can be 0. So we need to remove the else clause because it's not needed here and
            # it will raise an IndentationError exception because there is nothing after it that is indented once TAB.
            print(
                "No errors occurred"
            )  # Furthermore it can't capture any exception thrown because exceptions are caught by except clauses -
            # they are mutually exclusive and if an exception happens only an except clause catches it -
            # we can add multiple exception catches but unless you write code that causes them all to be thrown at
            # once no more than one of them will execute in most cases. (e.g. if you are dividing by zero twice it'll
            # only show Error 1: ZeroDivisionError - but what if you want to show both errors?
            # Like for example write them all to a file so you know where the errors came from and what caused them.
            # - in this case we will create a function to catch multiple exceptions called multi_exceptions)
            break

        finally:  # Bug in this line, finally clause executes code independent of how the try clause ends, so we need
            # to move all code dividing dividend by divider into this clause
            return  # Bug in this line and below, return inside the while loop is bad because it will stop the
            # program no matter which try/except has occurred and will be executed first. This can be fixed by
            # removing the return statement below and moving the input() functions out of the while loop
            # The finally clause is good for closing files in case you forget to close them after
            # using them, or at least that what I have seen it used for, but it can also be used as a catch all
            # exception catch. - like below
            time.sleep(
                10
            )  # Another good example would be time.sleep() because it will execute for 10 seconds even if our
            # program crashes during that time, which can help us identify what caused it to crash because we
            # can see which line it stopped on.

            # uncomment this if you want the function to exit right away or comment it out if you want it to delay by
            # 10 seconds when an exception occurs
            # return


display_welcome_message()
display_result()


# Instructions for this exercise:
# 1. Make sure you are using Pycharm
# 2. Make sure you are in debug mode by clicking on the green bug in the top right corner of your project's main window.
# 3. Click on "Debug"
# 4. Start modifying the code to solve bugs
# 5. Maybe watch a youtube video to learn more about programming if you are stuck here or there, or google
# something like what is an exception in programming or what is a debugging tool in Pycharm - you can do this during run
# time because it's fun to press pause and unpause and make your program execute different parts of your code, or add a
# break point by pressing F8 on your keyboard while your program is running in debug mode to focus on finding a
# specific bug
# 6. Fix all bugs
# 7. Rinse and repeat steps 3 - 4 until you understand what all the weird things written here means,
# or until you find this guide helpful
