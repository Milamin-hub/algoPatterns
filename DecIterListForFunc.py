def multyFunc(func):
    def dec(*args) -> int:
        res = args[0]
        for i in range(len(args)):
            if i != len(args)-1:
                res = func(res, args[i+1])
        return res
    return dec
    
@multyFunc
def mul(i, j):
    return i * j
    
@multyFunc
def add(i, j):
    return i + j
    
print(mul(1, 2, 3, 3))
print(add(1, 2, 3, 3))

print(mul(5, 3))
print(add(3, 3))