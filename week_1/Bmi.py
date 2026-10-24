name  = input("What is your name?")
print(f"Hello, {name}!")

age = int(input("What is your age (in years)?"))
print(f"You are {age} years old")

height = float(input("How tall are you in meters?"))
print(f" you are {height} meters tall")

weight = float(input("how much do you weight(in kilograms)?"))
print(f"you weigh {weight} kilograms")

bmi = weight  / (height ** 2)

print(f"Your BMI is {bmi:.2f}")
