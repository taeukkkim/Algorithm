class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        
        for i in s:
            if new_s and i == '#':
                new_s.pop()
            else:
                if i != '#':
                    new_s.append(i)
        
        for j in t:
            if new_t and j == '#':
                new_t.pop()
            else:
                if j != '#':
                    new_t.append(j)

        return new_s == new_t   