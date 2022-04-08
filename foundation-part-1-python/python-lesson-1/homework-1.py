""" Python Session 1 Homework Question 1 """

# QUESTION
# -----------------------------------------------------------------------------
# I am building some very high quality chairs and need exactly four nails for
# each chair. I've written a program to calculate how many nails I need to buy
# to build these chairs.

# chairs = '15'
# nails = 4
#
# total_nails = chairs * nails
#
# message = 'I need to buy {} nails'.format(total_nails)
#
# print('I need to buy {} nails'.format(message))


# OUTPUT
# -----------------------------------------------------------------------------
# I need to buy I need to buy 15151515 nails nails


# SOLUTION
# -----------------------------------------------------------------------------
# The chairs variable points to the STRING '15'. This should be an INTEGER.
# Also, the print message has already been created so there is no need to
# include the text again within the print function.

chairs = 15
nails = 4

total_nails = chairs * nails

message = 'I need to buy {} nails'.format(total_nails)

print(message)