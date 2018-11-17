import random

class Die:
    def __init__(self):
        self.__value = 1
    
    # this class only defines one attribute, the value attribute.
    @property # read-only!
    def value(self):
        return self.__value

    def roll(self):
        self.__value = random.randrange(1,7)
    
    # makes it easier to get the value
    def __str__(self):
        # defines a string representation of the object. return the value attribute
        return str(self.__value)
    
class Dice:
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)
    
    def rollAll(self):
        for die in self.__list:
            die.roll()

    # define the Dice Object as the iterator
    def __iter__(self):
        self.__index = -1 # initialize index for each iteration
        return self
    
    # define the method that gets the next Die Object
    def __next__(self):
        if self.__index == len(self.__list)-1:
            raise StopIteration
        self.__index += 1
        die = self.__list[self.__index]
        return die