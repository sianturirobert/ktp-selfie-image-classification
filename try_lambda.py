t = lambda x, y : x + y
print(t(4,5))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(25)

print(mydoubler(22))

hs = lambda x: x**3

print(hs(454684331))