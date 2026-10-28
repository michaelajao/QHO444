# outfile = open("philosophers.txt", "a")
# outfile.write('Albert camus\n')
# outfile.close()


# int()
# float()
# str(12)

openfile = open("numbers.txt", "w")

number1 = 45

openfile.write(str(number1) + "\n")
openfile.close()


inline = open("numbers.txt", "r")
number = int(inline.readline())

print(f"The number in the file is {number}")
print("The number in the file is ", number)

inline.close()