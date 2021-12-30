import bisect


def binSearch(nums,target):
    if len(nums)==0:
        return False
    mid=len(nums)//2
    if nums[mid]==target:
        return True
    elif nums[mid]>target:
        return binSearch(nums[:mid],target)
    else:
        return binSearch(nums[mid+1:],target)

if __name__ == '__main__':
    nums=[240, 242, 244, 244, 246, 246, 247, 249]
    print(binSearch(nums,250))