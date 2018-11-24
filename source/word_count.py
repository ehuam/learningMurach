def word_count(string):
    
    dictionary = {}
    temp = string.lower()
    split_on_space = temp.split()
    
    # sets up the dictionary with all the the words
    # bc of how dictionarys are set up with it won't have duplicates
    for words in split_on_space:
        dictionary[words] = 0
    
    # set up a counter
    for word in split_on_space:
        if word in dictionary:
            dictionary[word] += 1
    
#     print(dictionary)

# word_count("HEY HEY how are you doing hey hey")


dictionary = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
              'Kenneth Love': ['Python Basics', 'Python Collections', 'java']}

# values() returns an interable of all the values in the dictionary
# for i in dictionary.values():
#     print(i)

# # keys() returns an interable of all the keys in the dictionary
# for i in dictionary.keys():
#     print(i)

# # items() returns a tuple of key and value
# for i in dictionary.items():
#     print(i)
#     print(len(i[1]))


# courses = []
# for i in dictionary.values():
#     courses.extend(i)
# print(courses)

# course_counter = {}
# teacher_most_courses = ''
# counter = 0

# # fill the dictionary course_counter with the names of the teachers which is keys()
# for i in dictionary.keys():
#     course_counter[i] = 0

# # count the length of the classes, which is the value but value is an array
# for j in dictionary.items():
#     course_counter[j[0]] = len(j[1])

# # determine who has the the highest number of courses by looping through the iterable
# # and checking each object is greater than the one before it. so a number index has to be used

# for k in course_counter.items():
#     if k[1] >= counter:
#         print("i am evaluating", k[1], ' and ', counter)
#         # print(k[0], 'which is type:', type(k[0]))
#         teacher_most_courses = k[0]
#         print("i've set the teacher with the most courses to", teacher_most_courses)
#         counter = k[1]
#         print("i've set the counter to ", counter)  

# Initialize a counter to track the teacher with the highest number of courses
# highest_tally = 0
# rockstar = ""

# # For each teacher and their list of courses, compare to the current longest length of courses
# for teacher, course_list in dictionary.items():
#     print('teacher is ', teacher)
#     print('course list is ', course_list)
#     if len(course_list) > highest_tally:
#         # If this person teaches more than our current rockstar, then record
#         # this teacher as the rockstar and set the highest tally to the length of their course list
#         highest_tally = len(course_list)
#         rockstar = teacher
# print( rockstar)

list_of_list = []
for teacher, course_length in dictionary.items():
    list_of_list.append(teacher)
    list_of_list[teacher].append(course_length)
print(list_of_list)