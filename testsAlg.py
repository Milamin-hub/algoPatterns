from typing import List
from logcolors import Color
import random


def rNum(n) -> int:
    return random.randint(-n, n)


def baseTest(n: int=100, d: bool=True):
    # n is count of tests
    def decorator(function):
        def wrapper(*args) -> None:
            
            if d:   
                correct = '\n------------------Tests 100% passed----------------------'
                for i in range(n):
                    function(i)
                    print(f'End test number: {i + 1}')
                   
                print(Color('green', correct))

                return None
            else:
                return function(*args)
            
        return wrapper
    return decorator


def test_TwoSum(n: int=100, d: bool=True): 
    #n is count of tests, d = on tests or off tests
    def decorator(funct):
        @baseTest(n=n, d=d)
        def wrapper(*args) -> List[int]:
            if not d: # If Enable Tests
                return funct(*args)
            else:
                def repeatTest(i):
                    nums = [rNum(9) for i in range(abs(rNum(9)))] # -> random length and random num
                    target = rNum(9) # random sum
                    
                    print(Color('yellow', f'nums: {nums}\ntarget: {target}'))

                    if funct(nums, target) != None:
                        t1 = funct(nums, target)[0]
                        t2 = funct(nums, target)[1]

                        if nums[t1] + nums[t2] != target:
                            print(Color('red', f'test {i}: incorrect answer!'))
                            raise NotImplemented()
                        
                return repeatTest(*args)
        return wrapper
    return decorator


def test_IsPolindrome(n: int=100, d: bool=True): 
    #n is count of tests, d = on tests or off tests
    def decorator(funct):
        @baseTest(n=n, d=d)
        def wrapper(*args) -> List[int]:
            if not d: # If Enable Tests
                return funct(*args)
            else:
                def repeatTest(i):

                    num = rNum(999)

                    print(Color('yellow', f'num: {num}'))

                    val1 = bool(str(num) == str(num)[::-1])
                    val2 = bool(funct(num))

                    print(Color('yellow', f'result: {val2}'))
                    
                    if val1 != val2:
                        print(Color('red', f'test {i}: incorrect answer!'))
                        raise NotImplemented()
                    
                return repeatTest(*args)
        return wrapper
    return decorator