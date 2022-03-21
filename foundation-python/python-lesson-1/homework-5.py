""" Python Session 1 Homework Question 4 """

# QUESTION
# -----------------------------------------------------------------------------
# Complete a series of tasks to slice the string "Python".
wrd = "Python"


# SOLUTIONS
# -----------------------------------------------------------------------------
#Task 1 - Slice the word so that you get "thon".
ans_1 = wrd[2:]
print(ans_1)

#Task 2 - Slice the word until "o".(Pyth)
ans_2 = wrd[:-2]
print(ans_2)

# Task 3 - Now try to get "th" only.
ans_3 = wrd[2:4]
print(ans_3)

#Task 4 - Now slice the word with steps of 2, excluding first and last characters
ans_4 = wrd[1:-1:2]
print(ans_4)