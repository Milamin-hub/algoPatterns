def isValid(s: str) -> bool:
    for i in s:
        if '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return False if len(s) != 0 else True
