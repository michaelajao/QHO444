book_cover = input("what type of cover does the book have (hard/soft)")

if book_cover == "soft":
    
    bound = input("is the book perfect bound (yes / no)")
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
        
else:
    print("Books with hard covers can be more expensive!")