#  A Gentle Introduction to Python 2022. Robin Thibaut, Ghent University

# Awesome Python Tutorial For Beginners
# This is a tutorial of the Python Programming Language.
# This part is a gentle introduction on classes in Python.

# A **class** is similar to a blueprint or prototype -- it describes the nature of something that can be constructed
# into an object. In Python, a **class** is simply an object with some extra instructions which define some special
# behaviors when it is created into an object or constructed. The special behavior includes composing the class into
# the object and forming its initial state, as well as various class or static methods. A **class** does not need to
# have any methods at all, but most will have one or more. In Python, creating a class is easy, the syntax is similar
# to our use of 'function'. However, there are some differences, namely:

# * classes are not callable - they just remain as classes
# * classes may have objects created from them - instances of the class/object type
# * instances of classes seem to be mutable values while classes are immutable

# ### The blueprint or prototype that describes the nature of something is the **class**. ### When you create
# something based on this blueprint or prototype you create an **object**. ### The process of creating an object is
# called **Instantiation**. ### So, when you create an object you instantiate a class. ### First comes the **class**
# (aka. blueprint) and when you create things from that class you get a lot of objects (aka. things).

# The first thing that comes to mind is the word 'self'.
# All the member functions in class methods must have a self parameter.
# And the self parameter is used to access attributes and methods of the class.
# There is no fixed rule on how to call it, but it is a general convention to use self as the name.


class Person(object):

    # The constructor of class Person takes no arguments.
    # It will create an empty object with no name and no age attributes when no arguments are given.

    def __init__(self):
        print(f"Creating an empty object {self}")

    def smile(self):
        print("{self} says... I am smiling.")

    def bowHead(self):
        print("{self} says... I am bowing my head.")

    def greet(self):
        print("{self} says... Hello, how are you today?")

    # These functions/methods seem to be more generally called behaviors in the literature.
    # They represent how objects of this type respond to various external stimuli.

    def changeName(self, newName):
        self.name = newName

    def changeAge(self, newAge):
        self.age = newAge

    def displayAttrs(self):
        print('Attributes of object "{}" are:'.format(self))

        for attr in self.__dict__:
            print('"{attr}" = "{value}"'.format(attr=attr, value=getattr(self, attr)))

        if not self.__dict__:
            print("No attributes found.")

    # Some functions/methods are fairly generic like smile, bowHead and greet. But some have been added just
    # to this type of object like changeName and changeAge which can set its attributes 'name' and 'age'. Of course,
    # they could have been included in the constructor, but it may be considered more self-documenting to include them
    # separately.


#  Example of creating an object from the class Person
p = Person()
p.smile()
p.changeAge("Philip")
print(p.name)
