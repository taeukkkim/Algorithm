from typing import List

# 풀이 1
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        s = list(s)
        p = sorted(list(p))
        
        p_len = len(p)
        s_len = len(s)
        
        for i in range(s_len-p_len+1):
            if sorted(s[i:i+p_len]) == p:
                answer.append(i)
                
        return answer

# 풀이 2
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        
        p_len = len(p)
        s_len = len(s)
        
        p = Counter(p)
        
        for i in range(s_len-p_len+1):
            if i == 0:
                window = Counter(s[:p_len])
            else:
                window[s[i-1]] -= 1
                window[s[i+p_len-1]] += 1

            if window == p:
                answer.append(i)
                
        return answer