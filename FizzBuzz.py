from typing import List


def fizzBuzz(n: int) -> List[str]:
    world = 'FizzBuzz'
    nums = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            nums.append(world)
            continue
        elif i % 3 == 0:
            nums.append(world[:4])
            continue
        elif i % 5 == 0:
            nums.append(world[4:])
            continue
        
        nums.append(i)
    return nums