nums = range(1, 1000)

def isSimpleNum(num: int) -> bool:
    # num = num if num >= 0 else -num
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

res = list(filter(lambda x: isSimpleNum(x), nums))

print(res)                                                                                                                                                                                                                                                                                     
