import bisect


def binSearchRecur(nums,target):
    if len(nums)==0:
        return False
    mid=len(nums)//2
    if nums[mid]==target:
        return True
    elif nums[mid]>target:
        return binSearchRecur(nums[:mid],target)
    else:
        return binSearchRecur(nums[mid+1:],target)

def binSearchIter(nums,target):
    l=0
    r=len(nums)-1
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
    nums=[1,5,7,89,123]
    print(binSearchIter(nums,5))