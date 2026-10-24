eyes_look = input("where should i look?")

if eyes_look == "in the bedroom":
    print("Where in the bedroom should I look?")
    
    bedroom_look = input()
    if bedroom_look == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

elif eyes_look == "in the bathroom":
    print("Where in the bathroom should I look?")
    
    bathroom_look = input()
    if bathroom_look == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")
        
elif eyes_look == "in the living room":
    print("where in the living room should I look?")
    
    livingRoom_look = input()
    if livingRoom_look == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some living room stuff but no phone.")

else:
    print("I do not know where that is but I will keep looking.")
    
