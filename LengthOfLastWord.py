def lengthOfLastWord(s: str) -> int:
    max = 0
    for i in s.split():
        length = len(i) if len(i) > max else max
    return length


# def lengthOfLastWord(s: str) -> int:
#     return len(s.rstrip(' ').split(' ')[-1])

