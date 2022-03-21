""" Python Session 1 Homework Question 3 """

# QUESTION
# -----------------------------------------------------------------------------
# I have a lot of boxes of eggs in my fridge and I want to calculate how many
# omelettes I can make. Write a program to calculate this. Assume that a box of
# eggs contains six eggs and I need four eggs for each omelette, but I should
# be able to easily change these values if I want. The output should say
# something like "You can make 9 omelettes with 6 boxes of eggs".


# SOLUTION
# -----------------------------------------------------------------------------

no_of_boxes = 6
eggs_per_box = 6
eggs_per_omelette = 4

total_omelettes = no_of_boxes * eggs_per_box // eggs_per_omelette

message = f"You can make {total_omelettes} with {no_of_boxes} boxes of eggs."
print(message)