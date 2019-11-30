x = 28

if x < 0:
    print("x is less than 0")                      # executes only if x < 0
elif x == 0:
    print("x is zero")                 # if it's not true that x < 0, check if x == 0
elif x == 1:
    print("x is equal to 1")                    # if it's not true that x < 0 and x != 0, check if x == 1
else:
    print("none of the above is true")

name = "Sai"
if name == "Sai":
    print(True)
else:
    print(False)