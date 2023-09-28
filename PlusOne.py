from typing import List


nums = [1, 2, 4]

# def plusOne(digits: List[int]) -> List[int]:
#     carry = 1

#     for i in reversed(range(len(digits))):
#         carry, digits[i] = divmod(digits[i]+carry, 10)

#     return digits if not carry else [carry] + digits

def plusOne(digits: List[int]) -> List[int]:
    return [int(i) for i in str(int(''.join(list(map(lambda x: str(x), digits))))+1)]

print(plusOne(nums))
