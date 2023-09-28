from typing import List


def removeDuplicates(nums: List[int]) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]

        return j+1


# def removeDuplicates(nums: List[int]) -> int:
#     nums[:] = sorted(set(nums))
#     return len(nums) 