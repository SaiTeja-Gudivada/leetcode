class Solution:
    def reverseOnlyLetters(self, ss: str) -> str:
        s=[]
        for i in ss:
            s+=[i] 
        l=0
        h=len(s)-1
        while(l<h):
            if (65<=ord(s[l])<=90 or 97<=ord(s[l])<=122) and (65<=ord(s[h])<=90 or 97<=ord(s[h])<=122):
                s[l],s[h]=s[h],s[l]
                l+=1
                h-=1
            elif (65<=ord(s[l])<=90)!=True and (97<=ord(s[l])<=122)!=True:
                l+=1
            elif (65<=ord(s[h])<=90)!=True and (97<=ord(s[h])<=122)!=True:
                h-=1
                
        return(''.join(s)) 
