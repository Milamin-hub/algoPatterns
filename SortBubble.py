from typing import List


nums = [1, 5, 6, 7, 21, 89, 10, 34, 55, 13]

def sortBubble(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    return nums


# print(sortBubble(nums))