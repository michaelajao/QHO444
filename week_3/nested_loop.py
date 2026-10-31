# # rows = int(input("How many rows do you want?"))
# # columns = int(input("How many columns do you want?"))

# # # display a grid emoji ☺️ where the size matches the user input

# # for row in range(rows):
# #     for colunm in range(columns):
# #         print("☺️ ", end="")
# #     print()

# # The program should first ask the user to enter a sequence of characters consisting of dashes and two markers e.g. "X----X".
# # The program should then ask the user to enter a character representing the marker e.g. X.
# # The program should then count the number of dashes between the two markers.
# # Finally, the program should print the total number of characters between the markers.


# sequence = input("Enter a sequence of characters (e.g. X----X): ")

# user_input = input("Enter the marker character (e.g. X): ")

# # counting the number of dashes between the two markers

# count = 0
# for i in range(len(sequence)):
#     # print(f"Checking position {i}, character: {sequence[i]}")
#     for j in range(i + 1, len(sequence)):
#         # print(f"Checking position {j}, character: {sequence[j]}")
#         if sequence[i] == user_input and sequence[j] == user_input:
#             count = j -i - 1
#             print(f"The distance between the markers is {count}")
#             break
            
# print("Done")


