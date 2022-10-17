import bisect
import collections
from functools import *
import heapq
import itertools
from heapq import *
import math
import string
from decimal import Decimal
from math import gcd
from sortedcontainers import SortedList
from typing import List, Union, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def traverse(self):
        p = self
        while p != None:
            print(p.val, end="->")
            p = p.next


import random

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def merge(l:List[int],r:List[int])->List[int]:
            p,q=0,0
            ret=[]
            while p<len(l) and q<len(r):
                if nums[l[p]]<nums[r[q]]:
                    ret.append(l[p])
                    p+=1
                else:
                    ret.append(r[q])
                    q += 1
            while p<len(l):
                ret.append(l[p])
                p += 1
            while q<len(r):
                ret.append(r[q])
                q += 1
            return ret

        def mergeSort(array):
            if len(array)<=1:
                return array
            mid=len(array)//2
            l=mergeSort(array[:mid])
            r=mergeSort(array[mid:])
            return merge(l,r)

        indexs=[i for i in range(len(nums))]
        indexs=mergeSort(indexs)
        ans=[0 for _ in range(len(nums))]
        for i in range(len(indexs)):
            if i>0 and nums[indexs[i]]==nums[indexs[i]-1]:
                
            ans[indexs[i]]=i
        return ans

if __name__ == '__main__':
    solution = Solution()
    garbage = ["G", "P", "GP", "GG"]
    nums1 = [3, 2, 5]
    nums2 = [2, 2, 1]
    diff = 1

    root = TreeNode(1)
    root.left = 5
    n = 15
    nums = [8,1,2,2,3]
    print(solution.smallerNumbersThanCurrent(nums))
