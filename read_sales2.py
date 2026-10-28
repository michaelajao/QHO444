def main():
    
    sales_file = open("sales.txt", "r")
    
    total = 0.0
    
    for line in sales_file:
        
        total = total + float(line)
        
    print("Total sales: £", format(total, ".2f"), sep="")
    print(f"Total sales: £{total:.2f}")
    
    sales_file.close()
    
main()