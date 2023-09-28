def compress(txt: str) -> str:
    count = 0
    res = ''
    if len(txt) < 2:
        return txt
    txt += '.'
    for i in range(len(txt)):
        if i != len(txt)-1:
            if txt[i] == txt[i+1] and i != len(txt)-1:
                count += 1
            else:
                res += txt[i]
                if count > 0:
                    res += str(count+1)
                count = 0 
    return res

result = compress('aabbbbceeeeedddddaaaaaa')
print(result)

result = compress('aacaacc')
print(result)


        
