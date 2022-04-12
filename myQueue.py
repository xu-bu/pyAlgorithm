
import collections

#239 维护能输出最大值的队列
#这里实现的单调队列并不是把窗口中单调递减的值拿出来组成一个新队列，而是保证新入队的元素一直是单调队列中最小的值。同时这个队列没有维护窗口中的所有元素，因为没有必要
#1.pop(value)：如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作
#2.push(value)：如果push的元素value大于入口元素的数值，那么就将队列后端的元素弹出，直到push元素的数值小于等于队列入口元素的数值为止
class myQueue:
    def __init__(self):
        self.queue=collections.deque()

    def pop(self,val):
        if self.queue and val==self.queue[0]:
            self.queue.popleft()

    def push(self,val):
        while self.queue and val>self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)



    def getMax(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k==1:
            return nums

        monoQ=myQueue()
        for i in range(k):
            monoQ.push(nums[i])

        ans=[monoQ.getMax()]
        for i in range(k,len(nums)):
            willPop,willPush=nums[i-k],nums[i]
            monoQ.pop(willPop)
            monoQ.push(willPush)
            ans.append(monoQ.getMax())
        return ans

if __name__ == '__main__':
    solution=Solution()
    s = "abcabcabcabc"
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(solution.maxSlidingWindow(nums,k))