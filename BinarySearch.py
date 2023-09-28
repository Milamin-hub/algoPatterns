from typing import List


def searchInsert(nums: List[int], target: int) -> int:
        
        first=0
        last=len(nums)-1
        mid=(first+last)//2

        pf=0
        pl=len(nums)-1
        
        while(first<=last):

            mid=(first+last)//2

            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                pf=first
                first=mid+1
            else:
                pl=last
                last=mid-1

        mid=(pf+pl)//2

        if(nums[mid]>target):
            return mid
        else:
            return mid+1