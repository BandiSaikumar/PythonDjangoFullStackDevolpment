animals = ['elephant', 'lion', 'tiger', "giraffe"]  # create new list
print(animals)

animals += ["monkey", 'dog']    # add two items to the list
print(animals)

animals.append("dino")   # add one more item to the list using append() method
print(animals)

rem = [sub.replace("dino", "dinosaur") for sub in animals]
print("list after sub_string replacement:" +str(rem))