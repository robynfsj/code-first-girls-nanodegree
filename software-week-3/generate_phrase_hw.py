"""Software Week 3 Homework – Generate Phrase"""

# —————————————————————————————————————————————————————————————————————————————
# HOMEWORK TASK - CHECK IF CHARACTERS CAN GENERATE THE TARGET PHRASE

# You are given a string of available characters and a string representing a
# word or a phrase that you need to generate. Write a function that checks if
# you can generate the required word/phrase using the characters provided.
# If you can, then please return True, otherwise return False.
#
# NOTES:
#     You can only generate the phrase if the frequency of unique characters
#     in the characters string is equal or greater than the frequency in the
#     document (phrase) string.
#
# FOR EXAMPLE:
#     characters = "cbacba"
#     phrase = "aabbccc"
#
#     In this case you CANNOT create required phrase, because you are 1
#     character short!
#
# IMPORTANT:
#     The phrase you need to create can contain any characters including
#     special characters, capital letters, numbers and spaces.
#
#     You can always generate an empty string.
# —————————————————————————————————————————————————————————————————————————————

from collections import Counter


def generate_phrase(target, characters):
    """Checks if characters can be used to generate target word or phrase.

    Retrieves the quantity of each character in a target string and checks if
    this quantity is matched or exceeded in another string of provided
    characters. Function is case-sensitive and accepts special characters.
    Empty target strings return True.

    Args:
        target (str): the word or phrase wanting to be generated
        characters (str): the provided characters wanting to be used to
                          generate the target string

    Returns:
        bool: True if target can be generated from characters. False if target
              cannot be generated from characters.
    """
    target_count = Counter(target)
    char_count = Counter(characters)

    for key in target_count:
        if target_count[key] > char_count[key]:
            return False
    return True
