# # # # # Declare a variable to count the current number of iterations
# # # # iterations = 0

# # # # # Display ready message
# # # # print("Starting iterations...")
 
# # # # # Display the current count    
# # # # while iterations < 100000:

# # # #     # Update the current iteration count
# # # #     iterations = iterations + 1
# # # #     print(f"Current iteration: {iterations}")

# # # # # Display completion message
# # # # print(f"Completed {iterations}!")



# # # apples = 100

# # # user_input = int(input("How many apples should i remove?"))



# # # while apples > 0 and user_input > 0:
# # #     user_input = user_input - 1
# # #     apples = apples - 1
    
# # #     print(f"apples left: {apples}")
    
    
# # # print("All apples removed")
# # # print(f"Final state - Apples: {apples}, User moves left: {user_input}")


# # # apples = 0 

# # # user_input = int(input("How many apples should i remove?"))

# # # while apples < user_input:
    
# # #     apples = apples + 1
    
# # #     print(f"apples removed: {apples}")
    

# # # print("All apples removed")


# # # sum of the first 100 number 
# # user_input = int(input("Enter a number: "))
# # number = 0
# # sum = 0
# # print("Calculating the sum of the first 100 numbers")

# # while number < user_input:
    
# #     number += 1

# #     print(f"Current number: {number}")
# #     sum += number
    
# #     print(f"Current sum: {sum}")

# # print(f"Final sum: {sum}")

# for count in range(100):
#     print("#########")
#     print("#       #")
#     print("# O   O #")
#     print("|   V   |")
#     print("|  ---  |")
#     print("|_______|")
    
    
    
# for count in range(0, 100, 1):
#     print("#########")
#     print("#       #")
#     print("# O   O #")
#     print("|   V   |")
#     print("|  ---  |")
#     print("|_______|")




# The function
from unicodedata import name


def greet_user():
    print("Please enter your name")
    name = input()
    print("Hello", name)



greet_user()

greet_user()

greet_user()