

def climbStairs(n: int) -> int:

    tb=[1,1]

    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])

    return tb[-1]