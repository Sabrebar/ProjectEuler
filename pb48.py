s=0
for i in range(1, 1001):
    s = (s + i**i) % 10**10
print (s)