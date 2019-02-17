#!/usr/bin/env python 3

from datetime import datetime
"""
This is the business tier for a Task List Program.
The task list program can store one or more lists of tasks
Each List can contain zero or more tasks

We are going to need to work with calendar dates
"""

class TaskList:
    def __init__(self, name = "blank", task_count = 0):
        self.__name = name
        self.__tasks = dict()
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    def addTask(self, task):
        self.__tasks[task.name] = task.content

    def removeTask(self, index):
        self.__tasks.pop(index)

    # def sortByDate:

    # def sortByComplete:

class Task:
    def __init__(self, name, dueDate, complete = False):

        try:
            if dueDate != None:
                tuple_date = int(dueDate.split('/'))
                date = datetime(month = tuple_date[0], day = tuple_date[1], year = tuple_date[2])
                self.__dueDate = date
        except TypeError as e:
            print("You can't pass string types as a constructor for date parameter. must be int")

        self.__name = name
        self.__dueDate = dueDate
        self.__complete = complete

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        print("Task name: {0}".format(self.name))