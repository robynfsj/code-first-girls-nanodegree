""" Lesson 8 Exceptions and Debugging – Homework """

# Write a function that can read contents of a file and can handle cases when
# provided file name does not exist:
# – Handle Error cases gracefully, displaying an informative message to the user.
# – What Error type can we use here? (check Python documentation)

# Create function
def read_text_file(file_name):
    print(f"Opening file: {file_name}")
    try:
        with open(file_name, "r") as f:
            file_contents = f.read()
            print(f"Success! Here are the contents:\n"
                  f"{file_contents}")
    except FileNotFoundError as no_such_file:
        print(f"Sorry an error occurred:\n{no_such_file}")


# Check it works for files that exist
read_text_file('test-file.txt')

# Returns:
# Opening file: test-file.txt
# Success! Here are the contents:
# Hello.
# This is a file created for testing if my python homework is working.


# Check it works for files that don't exist
read_text_file('non-existent-file.txt')

# Returns:
# Sorry an error occurred:
# [Errno 2] No such file or directory: 'non-existent-file.txt'