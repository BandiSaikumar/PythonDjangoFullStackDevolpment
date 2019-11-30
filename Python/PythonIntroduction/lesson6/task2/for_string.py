content = "Hello, World!"

for ch in content:    # print each character from hello_world
    print(ch)

length = 0      # initialize length variable

# count how many characters are in the hello_world using loop
if len(content) == 0:
    length += 1     # add 1 to the length on each iteration

print(len(content))