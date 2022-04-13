class Solution:
    def trap(self, h: List[int]) -> int:
        pre=h.copy()
        suf=h.copy()
        ans=0
        
        
        for i in range(1,len(h)):
            if pre[i]<=pre[i-1]:
                pre[i]=pre[i-1]
        for i in range(len(h)-1,-1,-1):
            if suf[i]>=suf[i-1]:
                suf[i-1]=suf[i]
        suf[-1]=h[-1]
        for i in range(len(h)):
            ans+=(h[i]-min(suf[i],pre[i]))
        return(abs(ans))
