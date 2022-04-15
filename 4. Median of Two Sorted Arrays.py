arr=nums1+nums2
arr.sort()
l=0
h=len(arr)-1
mid=l+h>>1
if len(arr)%2==0:
    return((arr[mid]+arr[mid+1])/2)
else:
    return(arr[mid])
