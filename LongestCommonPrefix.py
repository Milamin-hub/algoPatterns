from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    for a in list(zip(*strs)): 
        if len(set(a)) == 1: 
            res += a[0]
        else: 
            return res
    return res
