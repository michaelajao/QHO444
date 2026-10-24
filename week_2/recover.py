# ask user what to do
activity = input("What should I do (recover/study)?")
    
# decide if user should recover or study
if activity == "recover":

    # ask user
    recover_by = input("How would you like to recover (sleep/socialise)?")
    
    # decide if user should sleep or socialise
    if recover_by == "sleep":
        print("zzzZZZzzz")
    else:
        print("I will text my friends!")
else:
    print("I will study")