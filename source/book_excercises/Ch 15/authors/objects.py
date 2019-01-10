class Book:
    def __init__(self, title="", authors=None):
        self.title = title
        self.authors = authors

    def getDescription(self):
        return self.title + " by " + self.authors

    def __str__(self):
        return self.title + " by " + str(self.authors)

class Author:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName
    
    def __str__(self):
        return self.firstName  + ' ' + self.lastName
        

class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)
    
    def __str__(self):
        author_names = ""

        if self.count == 1:
            author_names = str(self.__list[0])
        else:
            for author in self.__list:
                author_names += str(author) + ", "
        return author_names

    @property
    def count(self):
        return len(self.__list)

    def __iter__(self):
        self.__index = -1 # initialize index for each iteration and defining a private attribute named index
        return self # returns self to indicate the current object is the iterator
    
    def __next__(self):
        if self.__index >= (len(self.__list) -1):
            raise StopIteration()
        self.__index += 1
        author = self.__list[self.__index]
        return author
