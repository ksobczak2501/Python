def double(a):
    if (isinstance(a, (int, float))==1):
        return a, 2*a
    if (isinstance(a, list)==1):
        return 2*a, [x * 2 for x in a]
print(double(3.))
print(double([3]))
print(double([1, 2, 3]))