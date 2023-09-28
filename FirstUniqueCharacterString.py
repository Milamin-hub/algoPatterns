from collections import Counter


def firstUnique(s: str) -> int:
    st = Counter(s)
    for i in range(len(s)):
        if st[s[i]] == 1:
            return i
    return -1

# def firstUnique(s): # 60 times slower
#     for i in range(len(s)):
#         if s.count(s[i]) < 2:
#             return i
#     return -1

def test():
    n1 = "leetcode"
    n2 = "loveleetcode"
    n3 = "aabb"

    assert firstUnique(n1) == 0
    assert firstUnique(n2) == 2
    assert firstUnique(n3) == -1

# test()