import bisect
import collections
import copy
import functools
from functools import *
import heapq
import itertools
from heapq import *
import math
import string
from decimal import Decimal
from math import gcd
from typing import List, Union, Optional
from sortedcontainers import SortedList


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

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[0 for _ in range(cols+1)]
        # best, ops, second ops
        # if can trans to best, we need ops, otherwise, need second ops
        def getCol(col):
            count =collections.Counter(grid[row][col] for row in range(rows))
            best=max(count,key=count.get)
            bestOps=rows-count[best]
            del count[best]
            if len(count)>0:
                secondOps =rows- count[max(count, key=count.get)]
            else:
                secondOps=rows
            return {"best":best,"bestOps":bestOps,"secondOps":secondOps}
        # always need to know what we choose on right
        right=getCol(cols-1)
        dp[cols-1]=right["bestOps"]
        for col in reversed(range(cols-1)):
            cur=getCol(col)
            # if cur can choose best, we choose it simply then update what we choose on right
            if cur["best"]!=right["best"]:
                dp[col]=cur["bestOps"]+dp[col+1]
                right = cur
            # otherwise, we compare
            else:
                if cur["bestOps"]+right["secondOps"]+dp[col+2]>cur["secondOps"]+right["bestOps"]+dp[col+2]:
                    dp[col]=cur["secondOps"]+right["bestOps"]+dp[col+2]
                    right = cur
                else:
                    dp[col] = cur["bestOps"]+right["secondOps"]+dp[col+2]
                    right = cur

        return dp[0]

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 0, 0, 2]
    k = 4
    grid=[[1,9,7,7,9,8,3],[6,9,6,7,2,4,4],[1,1,3,6,6,6,7],[6,3,3,9,6,2,6],[8,6,2,9,7,1,4],[6,1,2,5,9,6,4],[1,5,1,9,8,6,0]]
    for each in grid:
        for each2 in each:
            print(each2,end=' ')
        print()
    print(solution.minimumOperations(grid))

