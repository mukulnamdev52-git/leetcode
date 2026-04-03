class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            s=sorted(s)
            t=sorted(t)
            if len(t)!=len(s):
                return False
            else:
                if sorted(s)==sorted(t):
                    return True
            return False           



