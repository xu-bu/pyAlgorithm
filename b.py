import collections
import heapq
import math
from typing import List
import string

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        prex=[]
        tmp=0
        for each in nums:
            tmp+=each
            prex.append(tmp)
        ans=nums[0]
        for i in range(1,n):
            cur=math.ceil(prex[i]/(i+1))
            ans=max(cur,ans)
        return ans

if __name__ == '__main__':
    solution = Solution()
    garbage = ["G","P","GP","GG"]
    nums1 = [3, 2, 5]
    nums2 = [2, 2, 1]
    diff = 1

    n = 15
    nums =[6,9,3,8,14]
    print(solution.minimizeArrayValue(nums))
