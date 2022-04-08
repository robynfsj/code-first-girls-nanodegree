"""Software Assessment - Robyn Seymour-Jones"""

"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialisation’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random


class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

        if student_id:
            self.student_id = student_id
        else:
            self.student_id = self.generate_id()

    @staticmethod
    def generate_id():
        return random.randint(1000, 10000)

    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return f"{self.name} {self.surname}"


class NanoStudent(CFGStudent):

    def __init__(self, specialisation, name, surname, age, email, student_id=None):
        super().__init__(name, surname, age, email, student_id)
        self.specialisation = specialisation
        self.course_grades = {}

    @staticmethod
    def generate_id():
        return f"NANO{random.randint(1000, 10000)}"

    def add_new_grade(self, assessment, grade):
        self.course_grades[assessment] = grade

    def get_course_grades(self):
        return self.course_grades


############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}




"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Did it this way first but then changed it into the list comprehension as the
# exam paper suggested this.
# def even_fibonacci_sum(limit):
#     even_fib_nums = []
#     for i in range(0, limit):
#         if fib(i) % 2 == 0:
#             even_fib_nums.append(fib(i))
#     return sum(even_fib_nums)


def even_fibonacci_sum(limit):
    even_fib_nums = [fib(i) for i in range(0, limit) if fib(i) % 2 == 0]
    return sum(even_fib_nums)


##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))  # should be 0




"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

"""
WORKINGS OUT

input
-----
 main array (must be larger or sub-sequence wouldn't fit into it)
 smaller array, which is potential sub-sequence

output
------
bool
True if it is a sub-sequence
False if it isn't a sub-sequence

algo
----
if length of main array is less than length of sub-arrary => return false

iterate through main array - for each value in main array
    if first value in sub-seq does not equal value in main array
        move on to next value in main array
        if first value never found in main array => return False
    if first value in sub-seq matches value in main array
        move on to next value in sub-seq AND next value in main array
        if all nums in sub-seq found in main array => return True
"""


def is_valid_subsequence(arr, sub_seq):
    # Save time checking the sub-sequence if it clearly can't fit into array.
    if len(arr) < len(sub_seq):
        return False

    sub_seq_idx = 0
    for val in arr:
        if sub_seq[sub_seq_idx] == val:
            sub_seq_idx += 1
            # If all of sub-sequence has been found:
            if sub_seq_idx == len(sub_seq):
                return True
    return False


### TESTS ####

array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, -2]

print(is_valid_subsequence(array1, sequence1))  # FALSE

array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [1, 6, -1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE

array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE




"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

"""
TASK 4 ANSWER


1. Single responsibility
------------------------
In terms of the SOLID principles, the class Employee breaks the single 
responsibility principle - a class should only have a single reason to change.

The first two methods (update_department and update_status) update instance 
attributes that contain data about the employee. 

In contrast, the next two methods (save_employee and remove_employee) are 
performing a different task - modifying the data in the DB. I would probably 
refactor methods that modify the DB into their own class called DbMessenger. 

print_employee_report is doing something else again - writing to a file. This 
could go in another class called something like Reports.


2. Documentation
----------------
Add docstrings to the class and methods so that anyone reading the code would 
be better able to quickly see what each one is doing.


3. Testing
----------
I wouldn't know just from this script if tests have been written, but good 
coding practice would mean that a test script is written containing tests that 
cover a variety of end cases for each of the methods. I would aks the person if 
they had done this and if their tests all passed.


4. Exception handling
---------------------
Put try/except statements into the program.


5. Active status
----------------
Change name of the instance attribute self.active_status to self.is_active and 
store a bool to this attribute instead of a string so that an employee would 
either have self.is_active = True or self.is_active = False. Refactor methods 
accordingly. (If business doesn't need specific details written out in string.)

This would prevent different users entering their own strings that could lead 
to problems later on. E.g. an inactive user could be entered as "inactive", 
"not active", "on leave", "not_active" etc. Using a bool makes it clearer and 
could help later on, e.g. if you want to get details of only active employees.


6. Order of parameters/attribute assignments in init
----------------------------------------------------
This isn't an important one, but if I was writing this code, I would put the 
values in a more logical order. E.g. id_ would usually come first in the DB so 
I would list id_ first, followed by name. It would just help with structuring 
the data in my mind. Also id_ and name are not changed by the program, so 
listing these first sort of puts them out of the way and you know you can 
concentrate on the other attributes.
"""
