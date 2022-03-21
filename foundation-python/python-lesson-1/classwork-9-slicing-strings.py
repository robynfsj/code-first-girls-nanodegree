"""Python Session 1 Classwork Exercise 9 - Slicing Strings"""

# QUESTION
# -----------------------------------------------------------------------------
# String slicing examples
#
# S = 'ABCDEFGHI'
#
# Slice at Beginning & End
#
# Omitting the start index starts the slice from the index.
# Meaning, S[:stop] is equivalent to S[0:stop]
#
# Omitting the stop index extends the slice to the end of the string.
# Meaning, S[start:] is equivalent to S[start:len(S)]


# SOLUTION
# -----------------------------------------------------------------------------
s = "abcdefghi"
slice_first_3 = s[3:]  
slice_last_3 = s[:-3]  

print(slice_first_3)  # defghi
print(slice_last_3)  # abcdef


# MY EXTRA NOTES
# -----------------------------------------------------------------------------
# I did this exercise wrong. When you are asked to slice something, it specifies
# the letters you want to keep not remove. So if you are asked to slice the 
# first three letters, it is asking you to slice and keep them, not slice them
# off and discard them (i.e. slice first three letters means retrieve the first 
# three letters - abc).
# It should be:

slice_first_3 = s[:3]
slice_last_3 = s[-3:]

print(slice_first_3)  # abc
print(slice_last_3)  # ghi

# We can also reverse a string using the following:
reverse = s[::-1]
print(reverse)  # ihgfedcba

# Note that the start number is inclusive but the stop number is exclusive.

# When we are slicing from the end (i.e. using -), the start number still goes 
# first (e.g. [-11:-7] not [-7:-11]).

# Think of the index as being between the characters! In the word "code" the 
# indicies would be:
# 0c1o2d3e4
# So if I am slicing the letters "od", I need to slice from index 1, which is 
# before the letter "o" to index 3, which is after the letter "d".
print("code"[1:3])  # od

# For negative indexing, the indicies would be:
# -4c-3o-2d-1e0
print("code"[-3:-1])  # od

# For reverse indexing, the indices would be:
# 3e2d1o0c
print("code"[2:0:-1])  # do
print("code"[3:1:-1])  # ed

# The number in the third position is the step. You can use it not just to 
# reverse the string but to skip over some characters.
print("code"[::2])  # cd


# PRACTICE
# -----------------------------------------------------------------------------
s = "Robyn Francesca Seymour-Jones"

# Slice Francesca from string s.
print(s[6:15])
print(s[-23:-14])

# Reverse string s.
print(s[::-1])

# Slice and reverse Francesca from string s.
# Note that when reversing, start and stop must be specified in reverse order,
# but the first number is still inclusive and the second number is still 
# exclusive. Very confusing! 
print(s[6:15])  # Francesca
print(s[14:5:-1])  # acsecnarF