count = 0
for i in range(5):
    if i == 3:
        count += 1
        continue   # skip the rest of the code inside loop for current i value
print(i)
count =0
for x in range(10):
    if x == 2:
        count += 1
        continue   # skip print(x) for this loop
print(x)
