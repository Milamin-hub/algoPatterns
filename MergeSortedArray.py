from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:] = nums2[:n]
    nums1.sort()


# def mergeArray(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     for i in range(n):
#         if n > 0:
#             cur = nums1.index(0)
#             num = nums2.pop()
#             nums1.pop(cur)
#             nums1.insert(cur, num)
#     nums1.sort()
