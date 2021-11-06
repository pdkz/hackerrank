from collections import Conter

def anagram(s):
    # Write your code here
    N = len(s)
    if N % 2 == 1:
        return -1
    
    m = N // 2
    s1 = Counter(s[:m])
    s2 = Counter(s[m:])
    
    return sum((s1 - s2).values())
