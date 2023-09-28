from testsAlg import test_TwoSum
from typing import List


@test_TwoSum(n=20,d=True) # test default True
def twoSum(nums: List[int], target: int) -> List[int]:
    res = dict() # save num: index

    for i, num in enumerate(nums):

        comp = target - num

        if comp in res: # search num: comp + num = target
            return [i, res[comp]]

        res[num] = i # save num: i, in dict

twoSum([2, -1, 7, 4], 6)