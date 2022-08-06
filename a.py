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

from typing import List,Union,Optional

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def traverse(self):
        p = self
        while p != None:
            print(p.val,end="->")
            p = p.next

import random


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        items=[]
        ans=[]
        def dfs(root:TreeNode):
            # if not root:
            #     return
            items.append(str(root.val))
            if not root.left and not root.right:
                ans.append(items[:])
                return
            if root.left:
                dfs(root.left)
                items.pop()
            if root.right:
                dfs(root.right)
                items.pop()
        dfs(root)
        ret=[]
        for each in ans:
            ret.append(('->').join(each))
        return ret

if __name__ == '__main__':
    solution=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(5)
    print(solution.binaryTreePaths(root))

