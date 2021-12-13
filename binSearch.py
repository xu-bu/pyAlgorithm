def binSearch(nums,target):
    n=len(nums)
    if n==0:
        return -1
    else:
        l,r=0,n-1
        #这个地方必须是小于等于，因为会有数组中只有一个数的情况
        while l<=r:
            mid = (l + r) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1

if __name__ == '__main__':
    nums=[1,2,3,5,67,90,104,678]
    print(binSearch(nums,2))