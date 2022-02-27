import bisect
import collections
import heapq
import string

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

if __name__ == '__main__':
    nums=[2,4]
    solution=MedianFinder()
    solution.addNum(1)
    solution.addNum(2)

    print(solution.findMedian())
    solution.addNum(3)
    print(solution.findMedian())