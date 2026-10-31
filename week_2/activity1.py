print("What type of cover does the book have (soft/hard)?")
book = input()

if book == "soft":
    
    print("Is the book perfect-bound (yes/no)?")
    perfect_bound = input()
    
    if perfect_bound == "yes" or perfect_bound == "y":
        print("Soft cover, perfect bound books are very popular!")
        
    elif perfect_bound == "no":
        print("Soft covers with coils or stitches are great for short books" )
        
else:
    print("Books with hard covers can be more expensive!")