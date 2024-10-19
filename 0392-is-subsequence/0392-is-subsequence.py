class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(t)
        r=""
        j=0
        i=0
        while i < n:
            if len(s)==0:
                break
            if j<len(s) and s[j]==t[i]:
                r+=t[i]
                j+=1
            i+=1
        if r==s:
            return True
        else:
            return False

        
        