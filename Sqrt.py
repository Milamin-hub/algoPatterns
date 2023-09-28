def mySqrt(x: int) -> int:

    if x < 2:
        return x

    l, r = 1, x // 2

    while l <= r:
        mid = (l + r) // 2

        sq = mid * mid

        if sq == x:
            return mid
        if sq > x:
            r = mid - 1
        else:
            l = mid + 1
            
    return r


# def mySqrt(x: int) -> int:
#     return int(pow(x, 0.5))

