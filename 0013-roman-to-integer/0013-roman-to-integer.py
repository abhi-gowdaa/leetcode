class Solution(object):
    def romanToInt(self, s):
        symbols={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ=0
        i=0
        n=len(s)
        while i<n:
            if i<n-1 and symbols[s[i]] < symbols[s[i+1]]:
                summ=summ+(symbols[s[i+1]]-symbols[s[i]])
                i+=2

            else:
                summ=summ+symbols[s[i]]
                i+=1
  
        return summ
                
            
        