def main():
    infile = open('philosophers.txt', 'r')
    
    # file_content = infile.read()
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()

    
    infile.close()


    print(line1)
    print(line2)
    print(line3)
    
    
    
main()



name1 = 'kritagya'

people = open("people.txt", "w")

people.write(name1 + "\n")
people.write("bhogindar" + "\n")

people.close()