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
    def __init__(self, dueDate=None, complete = False):
        try:
            if dueDate != None:
                tuple_date = int(dueDate.split('/'))
                date = datetime(month = tuple_date[0], day = tuple_date[1], year = tuple_date[2])
                self.__dueDate = date
            else:
                self.__dueDate = None
        except TypeError as e:
            println("You can't pass string types as a constructor. must be int")
    
        self.__complete = complete

        