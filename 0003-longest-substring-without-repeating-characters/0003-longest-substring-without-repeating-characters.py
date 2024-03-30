class Solution(object):
    def lengthOfLongestSubstring(self, input):
        
        box=[]  #list 
        n=len(input)
        length=0
        maxlength=0
        i=0
        j=0
        while j<n:
            if input[j] in box:
                box.pop(0) #we pop starting ele from list to recheck again 
                i+=1
                length=length-1  # we move left pointer(i) by 1 stepe so length should decrease by one 
            else:
                box.append(input[j])
                length=length+1
                maxlength=max(maxlength,length)
                j+=1
        return maxlength
        
        