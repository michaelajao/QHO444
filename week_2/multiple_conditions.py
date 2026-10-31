print("Enter the type of adventure you want to go on:(scary, short, long, and safe)")
adventure = input()

if adventure == "scary" or adventure == "short":
    print("Entering the dark forest")
    
elif adventure == "long" or adventure == "safe":
    print("Taking the safe route")
    
else:
    print("Not sure which adventure to take")