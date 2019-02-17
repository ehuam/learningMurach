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
    def __init__(self, name, dueDate, **kwargs):
        date = dueDate.split('/')
        self.name = name
        self.dueDate = datetime(month = int(date[0]),
                                day = int(date[1]),
                                year = int(date[2]))
        self.__complete = False       

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def setDate(self, date):

        date = int(dueDate.split('/'))
        self.dueDate.replace(month = date[0],
                             day = date[1],
                             year = date[2])

    def __str__(self):
        return ("Task name: {0} Due Date: {1} Complete: {2}".format(self.name, self.dueDate, self.__complete))