from string import ascii_letters as lt
from collections import Counter


lt = Counter(lt.lower())
lt.__add__('ags')
print(lt)