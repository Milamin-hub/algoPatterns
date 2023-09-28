from typing import List


nums = [3, 2, 2, 3, 1, 4, 3]
val = 3

def removeElement(nums: List[int], val: int) -> int:
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    
    nums[:] = nums[:i] # [2, 2, 2, 3] -> [2, 2], i = 2
    return nums

# def removeElement(nums: List[int], val: int) -> List[int]:
#     while val in nums:
#         nums.remove(val)

#     return nums

print(removeElement(nums, val))




