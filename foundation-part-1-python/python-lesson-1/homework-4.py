""" Python Session 1 Homework Question 4 """

# QUESTION
# -----------------------------------------------------------------------------
# Complete a series of tasks to format strings


# SOLUTIONS
# -----------------------------------------------------------------------------
# Task 1 - Replace the (.) with (!)
my_str_1 = "I love coding."

ans_1 = my_str_1.replace(".", "!")
print(ans_1)

# Task 2 - Reassign str so that, all its characters are lowercase.
my_str_2 = "EVERY Exercise Brings Me Closer to Completing my GOALS."

ans_2 = my_str_2.lower()
print(ans_2)

# Task 3 - Does the string start with an A?
my_str_3 = "We enjoy travelling"

ans_3 = my_str_3[0] == "A"
print(ans_3)

# Task4 - What is the length of the given string?
my_str_4 = "1.458.001"

ans_4 = len(my_str_4)
print(ans_4)