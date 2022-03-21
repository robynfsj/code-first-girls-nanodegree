""" Python Session 1 Homework Question 2 """

# QUESTION
# -----------------------------------------------------------------------------
# I'm trying to run this program, but I get an error.
# What is the error telling me is wrong?
# How do I fix the program?

# my_name = Penelope
# my_age = 29
#
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)
# print(message)


# OUTPUT
# -----------------------------------------------------------------------------
# NameError: name 'Penelope' is not defined


# SOLUTION
# -----------------------------------------------------------------------------
# Penelope needs to be a string.

my_name = "Penelope"
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)