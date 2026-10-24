first_num = int(input("please enter first number: "))
second_num = int(input("please enter second number: "))

# program should decide whihc of the number is the smallest and display the message
if first_num < second_num:
    print("The first number is the smallest!")
elif second_num < first_num:
    print("The second number is the smallest!")
elif first_num == second_num:
    print("Both numbers are equal!")
    
print("finished checking the numbers")