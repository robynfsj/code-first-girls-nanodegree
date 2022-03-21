"""Python Session 1 Classwork Exercise 4 - String Methods"""

# QUESTION
# -----------------------------------------------------------------------------
# EXAMPLES OF STRINGS METHODS
# Watch the demos


# DEMO 1 - .format()
# -----------------------------------------------------------------------------

# Define the variables
oranges = 12
cost_per_orange = 0.5

# Calculate the total cost for 12 oranges
total_cost = oranges * cost_per_orange

# Create a new variable call output that we will use for the print statement
output = str(oranges) + " oranges cost £" + str(total_cost)
print(output)

# We don't really need the variable output. Could just write:
print(str(oranges) + " oranges cost £" + str(total_cost))

# Python strings have a method (.format()) that substitues placeholders {} for
# values.
output = "{} oranges cost £{}".format(oranges, total_cost)
print(output)

# Another way to write the above code and is considered easier to understand
# by many
output = f"{oranges} oranges cost £{total_cost}"
print(output)


# DEMO 2 - .join()
# -----------------------------------------------------------------------------

# We need to join a few strings together. These strings are contained in a
# list [] or tuple (). We need to specify the string symbol that we want to
# be placed between the individual strings in the new string. It is this
# separator that the .join() method is working on.

# .join() with lists
num_list = ['1', '2', '3', '4']
separator1 = ' - '
output1 = separator1.join(num_list)
print(output1)

# .join() with tuples
num_tup = ('1', '2', '3', '4')
separator2 = ' => '
output2 = separator2.join(num_tup)
print(output2)

# You can use another string variable as the separator
s1 = 'abc'
s2 = '123'
print(s1.join(s2))
print(s2.join(s1))