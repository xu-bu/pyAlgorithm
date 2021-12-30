
#将排好序的两个数组合并,并返回这个排好序的数组
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

a = [4, 7, 8, 3, 5, 9]
print(mergeSort(a))