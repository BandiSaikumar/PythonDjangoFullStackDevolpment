animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']   # create new list
print(animals)

rem = [sub.replace("lion","cat") for sub in animals]    # replace 2 items -- 'lion' and 'tiger' with one item -- 'cat'
print("list after relacing sub_string:"+str(rem))

x = animals[4:] + animals[:2]    # remove 2 items -- 'cat' and 'giraffe' from the list
print(x)

animals.clear()
print("After the list is clear:",animals)