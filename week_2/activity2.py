print("Where should I look?")

location = input()

if location == "in the bedroom":
    print("Where in the bedroom should I look?")
    
    bedroom_location = input()
    
    if bedroom_location == "under the bed":
        
        print( "Found some shoes but no phone")
        
    else:
        print("Found some mess but no phone.")
        
elif location == "in the bathroom":
    print("Where in the bathroom should I look?")
    
    bathroom_location = input()
    
    if bathroom_location == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")
        
elif location == "in the living room":
    print("Where in the living room should I look?")
    
    living_room_location = input()
    
    if living_room_location == "on the table":
        
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
        
else:
    print("I do not know where that is but I will keep looking." )