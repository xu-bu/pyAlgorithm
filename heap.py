import bisect
import collections
import heapq
import string

#heapify之后的数组自身是无序的，但是它能保证堆顶位置的元素（即heap[0]）一定是最小的，所以涉及到一串数组慢慢输入，求过程中最值的问题，可以考虑堆排序

#维护一个能输出中位数的列表
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap=heapq.heapify([])
        #大根堆 负责放较小的数
        self.maxHeap = heapq.heapify([])


    def addNum(self, num: int) -> None:
        if len(self.maxHeap)==len(self.minHeap):
            #先放到大根堆中，再把大根堆根元素pop到小根堆中
            #如果num理应被添加到大根堆中，显然成功。如果理应被添加到小根堆中，则num会变为大根堆的根元素，然后被pop到小根堆中
            #使用puhspop，效率更高
            heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap,num))
        #由于当两个堆中元素数量一致时，总是在把元素往小根堆里放，所以nums为奇数个数时，小根堆里的数多一些，应该把元素放到大根堆中
        else:
            heapq.heappush(self.maxHeap,-heapq.heappushpop(self.minHeap,num))


    def findMedian(self) -> float:
        if len(self.maxHeap)==len(self.minHeap):
            return (self.minHeap[0]+self.maxHeap[0])/2
        else:
            return self.minHeap[0]

class Solution:
    #502 IPO
    #当给出一串输入数字，一个一个往列表中输入，同时还需要保证列表的顺序时，使用堆的效率很高
    def findMaximizedCapital(self, k, w, profits, capital):
        n = len(profits)
        if w>=max(capital):
            return sum(heapq.nlargest(k,profits))+w
        arr=[(capital[i],profits[i]) for i in range(n)]
        arr.sort(key=lambda x:x[0])
        canProfit=[]
        index = 0
        for i in range(k):
            while index < n and arr[index][0]<=w:
                heapq.heappush(canProfit,-arr[index][1])
                index+=1
            if len(canProfit) == 0:
                return w
            # 选择canProfit列表中收益最高的项目投资
            w -= heapq.heappop(canProfit)
        return w

    def findKthLargest(self, nums: list[int], k: int) -> int:
        #小根堆只存k个
        minH=[]
        heapq.heapify(minH)
        # maxH=heapq.heapify([])
        for i in range(k):
            heapq.heappush(minH,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>minH[0]:
                heapq.heappop(minH)
                heapq.heappush(minH,nums[i])
        return minH[0]


if __name__ == '__main__':
    nums=[3,2,3,1,2,4,5,5,6]
    solution=Solution()
    print(solution.findKthLargest(nums,4))