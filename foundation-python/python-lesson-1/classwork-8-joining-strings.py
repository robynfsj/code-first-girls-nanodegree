"""Python Session 1 Classwork Exercise 8 - Joining Strings"""


# DEMO
# -----------------------------------------------------------------------------

# We need to join a few strings together. These strings are contained in a
# list [] or tuple (). We need to specify the string symbol that we want to
# be placed between the individual strings in the new string. It is this
# separator that the .join() method is working on.

# .join() with lists
num_list = ['1', '2', '3', '4']
separator1 = ' - '
output1 = separator1.join(num_list)
print(output1)  # 1 - 2 - 3 - 4 

# .join() with tuples
num_tup = ('1', '2', '3', '4')
separator2 = ' => '
output2 = separator2.join(num_tup)
print(output2)  # 1 => 2 => 3 => 4

# You can use another string variable as the separator
s1 = 'abc'
s2 = '123'
print(s1.join(s2))  # 1abc2abc3
print(s2.join(s1))  # a123b123c

# The join method is applied to the string you want to be inserted between
# the characters of the string that is provided as an argument.


# QUESTION
# -----------------------------------------------------------------------------
# Perform string formatting, so that your final sentence looks like this:
# "We are going to cinema with my classmates: Mary, Pete, Eoin and me"

# This question is difficult to understand. It wants you to turn the list
# ["Mary", "Pete", "Eoin"] into a string using the .join() method.

guests = ["Mary", "Pete", "Eoin"]


# SOLUTION
# -----------------------------------------------------------------------------

separator = ', '
guest_string = separator.join(guests)
output = f"We are going to the cinema with my classmates: {guest_string} and me"

print(output)