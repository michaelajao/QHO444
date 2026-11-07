# # ***
# # The program should start by defining a function that has the name listen and which takes 0 parameters.
# # The function should do the following:
# #     Ask the user to enter a word representing a sound.
# #     Display the message "That was a loud" followed by the word entered by user and an exclamation mark.
# # Finally, the program should contain a call to your function listen



# # An example run of such a program is shown below:

# # What sound did you hear?
# # rumble

# # That was a loud rumble!


# def listen():
#     sound = input("What sound did you hear?\n")
#     print(f"That was a loud {sound}!")
    
    
# listen()

# def sound_indentifier(sound):
#     identify = input("What do you see?\n")
    
#     if identify == "a large boulder":
#         print("It is time to runnnnnnnng!!!!!!!!!")
#     else:
#         print("We will be fine.")
        
#     return print(f"You heard a {sound}.")
    

# sound_indentifier("breaking of rocks")


# def sum_squares(a, b, c):
    
#     sum = a**2 + b**2 + c**2
#     return print(sum)
    
    
# sum_squares(3, 9, 5)


# def display_box(name):
#   message = f"* Hello {name} *"
#   print("*" * len(message))
#   print(message)
#   print("*" * len(message))
  
# def greet_user():
#   print("Please enter your name")
#   name = input()
#   display_box(name)
  
# greet_user()


def listen():
  print("What sound did you hear?")
  sound = input()
  print(f"That was a loud {sound}!")
  
  

listen()