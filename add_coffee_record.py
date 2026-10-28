def main():
    
    another = "y"
    
    coffee_file = open("coffee.txt", "w")
    
    while another == "y" or another == "Y":
        
        print("Enter the following coffee data:")
        
        descr = input("Description: ")
        qty = int(input("Quantity (in kg): "))
        
        coffee_file.write(descr + "\n")
        coffee_file.write(str(qty) + "\n")
        
        another = input("Do you want to enter another record? (y/n): ")
    
    coffee_file.close()
    print("Coffee records have been added.")

main()