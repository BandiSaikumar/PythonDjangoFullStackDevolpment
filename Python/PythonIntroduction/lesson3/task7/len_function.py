phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
count = 0
for i in phrase:
    if i == 'r':
        count += 1
print(" count of r in phrase is: "+str(count))
length = len(phrase)
print(length)