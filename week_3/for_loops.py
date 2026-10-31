# # # # # # a programe to display some ascii mountains.

# # # # # user_input = int(input("How many mountains should I display?"))

# # # # # for count in range(user_input):
# # # # #     print("    __  ")
# # # # #     print("   /  \\__ ")
# # # # #     print("  /^      \\ ")
# # # # #     print(" /  ^       \\ ")
    
# # # # #     print("/           \\ ")
# # # # #     print("-------------")
    

# # # # user_input = int(input("How far are we from the target?"))

# # # # for count in range(user_input, 0, - 1):
# # # #     print(f"{count} steps remaining")
# # # # print("Target archieved!")

# # # print("Please enter a word")
# # # user_word = input()

# # # for position in range(0, len(user_word), 1):
# # #     print(user_word[position])
    
    
# # # #
# # # create a program that allows us to display a word character by character.

# # word = str(input("what word do you see?"))


# # print("Displaying index positions of each character")

# # for index in range(0, len(word), 1):
# #     print(f"Index {index}: {word[index]}")
    
# # print("Done!!!")


# for number in range(0, 10, 1):
#     print(f"{number} |", end="")


for count in range(0, 3, 1):
    for number in range(0, 10, 1):
        print(f"{number} |", end="")
    print(f"count {count}")