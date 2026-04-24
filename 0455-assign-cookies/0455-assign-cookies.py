class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        m=len(s)
        s.sort()
        g.sort()
        i=0
        j=0
        count=0
        while i<n and j<m:
            if s[j] >= g[i]:
                count+=1
                i+=1
            j+=1
        return count         

        




        