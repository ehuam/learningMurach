#!/usr/bin/env python 3

from calendar import Calendar

"""
This is the business tier for a Task List Program.
The task list program can store one or more lists of tasks
Each List can contain zero or more tasks

We are going to need to work with calendar dates
"""

class TaskList:
    def __init__(self, name = "blank", task_count = 0):
        self.__name = name
        self.__tasks = []

    def addTask(self, task):
        self.__tasks.append(task)

    def removeTask(self, index):
        self.__tasks.pop(index)

    # def sortByDate:

    # def sortByComplete:

class Task:
    def __init__(self, dueDate = )