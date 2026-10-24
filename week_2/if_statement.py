# take the user input
book = input("what type of book is this?")
#print the user input
print(book)

#check the  user input against our list of preferred genres
if book == "adventure" or book == "comedy":
    
    #print a message indicating that we like this genre of book
    print(f"i like {book} books")
    
#print a message indicating that we have finished reading the book
print("finished reading the book")