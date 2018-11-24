def packer(**kwargs):
    print(kwargs)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

teacher = {'name':"Kenneth", 'num':42, 'spanish_inquisition':None}

# packer(**teacher)
# unpacker(**{"last_name": "Love", "first_name": "Kenneth"})

# Unpacking a dictionary - pulling multiple keys and their values out of a 
# dictionary to feed them to a function

my_dictionary = {"name": "Edgar"}
# print("Hi, my name is {name}!".format(**my_dictionary))

# Packing a dictionary - putting multiple keyword arguments into a single dictionary.

def packing(**kwargs):
    print('the length of kwargs is', len(kwargs))

student = {'name': 'Edgar', 'age':29, 'sex':'male'}

# packing(**student)

course_minutes = {'Python Basics': 232, 'Django Basics': 237, 'Flask Basics': 189, 'Java Basics': 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long". format(course,minutes))
