"""Python Session 1 Classwork Exercise 7 - String Formatting"""

# QUESTION
# -----------------------------------------------------------------------------
# In a new Python file called cat_food.py, create a program that calculates how
# many cans of cat food you need to feed 10 cats. You will need:
# - A variable for the number of cats
# - A variable for the number of cans each cat eats in a day
# - A print() function to output the result
#
# Extension: change the calculation to work out the amount needed for 7 days


# SOLUTION
# -----------------------------------------------------------------------------
no_of_cats = 10
cans_per_day = 2

cans_required = no_of_cats * cans_per_day
message = "{} cats will require {} cans of food per day." \
      .format(no_of_cats, cans_required)

print(message)

# Note there are several different ways to use string formatting.

# Old style
print("%i cats will require %i cans of food per day." % (no_of_cats, cans_required))

# New style
print("{} cats will require {} cans of food per day.".format(no_of_cats, cans_required))

# Formatted string literals (f-strings)
print(f"{no_of_cats} cats will require {cans_required} cans of foot per day.")



# EXTENSION
# -----------------------------------------------------------------------------
no_of_cats = 10
cans_per_day = 2
no_of_days = 7

cans_required = no_of_cats * cans_per_day * no_of_days
message = f"{no_of_cats} cats will require {cans_required} cans of food per {no_of_days} days."

print(message)
