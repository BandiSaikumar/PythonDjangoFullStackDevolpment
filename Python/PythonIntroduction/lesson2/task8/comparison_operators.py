a = 5
b = 10
c = 15

print(c > b > a)
print(a < b < c)    # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.

lesser = b <= c
greater = c >=b

print(lesser)
print(greater)