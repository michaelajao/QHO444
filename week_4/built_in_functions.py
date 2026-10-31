# We wish to create a program that determines the ASCII code for a character.

# Start by creating a new folder called week4 inside of which you should create a file called built_in_functions.py.

# The program should start by displaying the message "Program Started!".
# The program should start by displaying the message "Please enter a standard character:".
# The program should then read in the user's response which should be a single character.
# The program should then check that a single letter has been entered using the built-in function len() . 
# If the length is 1 then the program should
#     determine the ASCII code of the character using the built-in function ord().
#     display the message "The ASCII code for {letter} is {value}." where {letter} is the letter entered by the user and {value} is the ASCII code as a number.
# Otherwise, if the length is not 1 then the program should
#     display a suitable error message
# Finally, the program should display the message "Program Ended!".



# An example run of such a program is shown below:

# Program Started!
# Please enter a letter:
# t
# The ASCII code for t is: 116
# Program Ended!
# Code your solution and be sure to include appropriate comments in your code.

# # display a message program started
# print("program started..........!")

# # read the user's input for a standard character
# character = input("Please enter a standard character: ")

# # check if a single input has been entered using len()
# if len(character) == 1:
    
#     # if the length of the input is 1, determine the ASCII code using ord() and display it
#     ascii_code = ord(character)
#     print(f"The ASCII code for {character} is {ascii_code}.")
# else:
#     print("Error: Please enter a single character.")

# print("Program Ended!")


def ascii_code_collector():
    # read the user's input for a standard character
    character = input("Please enter a standard character: ")

    # check if a single input has been entered using len()
    if len(character) == 1:
        
        # if the length of the input is 1, determine the ASCII code using ord() and display it
        ascii_code = ord(character)
        print(f"The ASCII code for {character} is {ascii_code}.")
    else:
        print("Error: Please enter a single character.")


# call the function to test it
ascii_code_collector()
ascii_code_collector()
ascii_code_collector()
ascii_code_collector()
ascii_code_collector()
ascii_code_collector()
