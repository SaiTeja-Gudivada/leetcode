ans=0
c=1
n=0
z=0
for i in nums:
    ans^=i
while(ans):
    r=ans&1
    ans=ans>>1
    if r:
        break
    c+=1
for i in nums:
    x=i
    x=x>>(c-1)
    #for j in range(c-1):
     #   x=x>>1
    if x&1==0:
        z^=i
    else:
        n^=i

return [n,z]
