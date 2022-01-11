
#将排好序的两个数组合并,并返回这个排好序的数组
import random
import time


def merge(leftList,rightList):
    l=r=0
    result=[]
    while l<len(leftList) and r<len(rightList):
        if leftList[l]<rightList[r]:
            result.append(leftList[l])
            l+=1
        else:
            result.append(rightList[r])
            r += 1
    for each in rightList[r:]:
        result.append(each)
    for each in leftList[l:]:
        result.append(each)
    return result

#主函数只有两个部分，首先写递归出口，如果没有return，就把数组分成左右两块，分别把这两块排好序然后合并
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    else:
        mid=len(nums)//2
        #将数组分成两块，分别排好序，然后拼起来
        leftList=mergeSort(nums[:mid])
        rightList=mergeSort(nums[mid:])
        return merge(leftList,rightList)



def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


n=100000
# nums=[]
# for i in range(1,n):
#     nums.append(random.randint(1,i))
# startTime=time.time()
# mergeSort(nums)
# print(f"mergesort runs for {time.time()-startTime}s")
#
nums=[]
for i in range(1,n):
    nums.append(random.randint(1,i))
startTime=time.time()
print(f"quicksort runs for {time.time()-startTime}s")

nums=[]
for i in range(1,n):
    nums.append(random.randint(1,i))
startTime=time.time()
sorted(nums)
print(f"sort runs for {time.time()-startTime}s")