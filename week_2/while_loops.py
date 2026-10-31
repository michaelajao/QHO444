# robot = int(input("How many apples should I remove?"))
# apples = 100

# while apples > 0 and robot > 0:
#     apples = apples - 1
#     robot = robot - 1
    
#     print(f"Apples left: {apples}, Robot moves left: {robot}")
# print("All apples removed")
# print(f"Final state - Apples: {apples}, Robot moves left: {robot}")

user_input = int(input("How many apples should I remove?"))
apple = 0

while apple < user_input:
    apple = apple + 1
    print(f"robot removed: {apple}")
print("All apples removed")