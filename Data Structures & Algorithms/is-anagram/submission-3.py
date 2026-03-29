class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prevMap={}
        if len(s)==len(t):
            for i in s:
                if i not in t or s.count(i)!=t.count(i):
                    return False
            return True 
        return False