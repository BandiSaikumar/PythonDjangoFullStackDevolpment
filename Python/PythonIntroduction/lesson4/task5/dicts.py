# create new dictionary.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" are keys and numbers are values
print(phone_book)

# Add new item to the dictionary
phone_book.update({"Jill": 345})
print(phone_book)

# Remove key-value pair from phone_book
for key in phone_book.keys():
    if key == 'john':
        del phone_book[key]
# phone_book.pop({"John": 123})
# print(phone_book)

print(phone_book.get("jane"))
print("jane" in phone_book.values())