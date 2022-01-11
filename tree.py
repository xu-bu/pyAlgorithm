import collections
from queue import Queue


class TreeNode:
    val=0
    left,right=None,None

    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left,self.right=left,right

#通过root遍历一棵树，初始队列只有根节点，count从0开始递增，每次将queue[count].val加入到输出中，同时将被遍历的节点的孩子节点全部加入到queue中，如果遍历到空节点，则向输出中加入null，直到count==len(queue)
def TreeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    #-2是因为逗号后面还有空格
    return "[" + output[:-2] + "]"

#对列表中的每个根节点进行TreeNodeToString
def TreeNodeArrayToString(TreeNodeArray):
    serializedTreeNodes = []
    for TreeNode in TreeNodeArray:
        serializedTreeNode = TreeNodeToString(TreeNode)
        serializedTreeNodes.append(serializedTreeNode)
    return "[{}]".format(', '.join(serializedTreeNodes))

#前序遍历
def traverse(head:TreeNode):
    if head==None:
        return
    else:
        print(head.val)
        traverse(head.left)
        traverse(head.right)

#递归层次遍历
def visitLevel(head:TreeNode,level):
    if head == None:
        return
    elif level==1:
        print(head.val)
    else:
        visitLevel(head.left,level-1)
        visitLevel(head.right,level-1)

def countHeight(head:TreeNode):
    if head == None:
        return 0
    else:
        left = countHeight(head.left)
        right = countHeight(head.right)
        return max(left, right) + 1

def countNode(head):
    if head==None:
        return 0
    else:
        return countNode(head.left)+countNode(head.right)+1

#检查以上算法时只考虑四种情况：
# 1.没有子节点的叶子节点
# 2.只有一个孩子节点的叶子节点
# 3.有两个孩子节点的叶子节点
# 4.任意二叉树的根节点

def isFullBtree(head:TreeNode):
    if pow(2,countHeight(head))-1==countNode(head):
        return True
    else:
        return False

# 层次遍历二叉树的节点（包括空节点），全部放到一个队列里，会发现以下规律：
#
# A B C D E F G 0 0 0 0 0 0
#
# 规律就是前面是非空节点，而后面是空节点。如果是非完全二叉树呢，那么出现以下现象：
#
# A B 0 0 C D 0 0 E F G
def isCompleteTree(head:TreeNode):
    if head==None:
        return True
    else:
        q=Queue()
        q.put(head)

        while(p:=q.get()):
            q.put(p.left)
            q.put(p.right)
        while(not q.empty()):
            p=q.get()
            if(p!=None):
                return False
        return True

#98
def isValidBST(node, lower=float('-inf'), upper=float('inf')) -> bool:
    #如果遍历到空节点，什么整棵树都满足了，return true
    if not node:
        return True
    #检查自己与自己的父节点的关系
    val = node.val
    if val <= lower or val >= upper:
        return False
    #检查左右子树，如果是右孩子，需要比自己大，所以自己是下界，上界不变。左孩子反之
    if not isValidBST(node.right, val, upper):
        return False
    if not isValidBST(node.left, lower, val):
        return False
    return True

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution:
    #95
    def generateTrees(self,n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        #根据[start,end]中的数生成所有可行的bst,返回存有这些bst的根节点的列表
        def generate(start,end):
            if start>end:
                #返回空节点，在start==end的情况，根节点的孩子节点就是两个这个的空节点
                return [None]
            #每一次generate可行bst列表的时候，[start,end]都不同，所以需要重置ans
            ans = []
            for i in range(start,end+1):
                #根节点为i的时候，生成左右子树列表
                leftTrees=generate(start,i-1)
                rightTrees=generate(i+1,end)
                for l in leftTrees:
                    for r in rightTrees:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        ans.append(root)
            return ans
        return generate(1,n) if n else []

    #99 中序遍历bst，其结果一定是从小到大
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        t1=t2=pre=None

        def inOrder(root):
            nonlocal t1,t2,pre
            if not root:
                return
            inOrder(root.left)
            #不断拿数和它前面的数比，第一次发现有数比前面的数小，说明它前面的数位置不对，第二次发现时，说明自己的位置不对。但特殊情况是只有两个数，所以干脆第一次发现时就把pre和cur都当作有问题的，后面再发现有问题的，就赋值给t2
            if pre!=None and root.val<pre.val:
                if not t1:
                    t1=pre
                t2=root
            pre=root
            inOrder(root.right)

        inOrder(root)
        t1.val,t2.val=t2.val,t1.val
        return root
#102
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[root]
        item = []
        ans = []
        index,cur,next,count,size=0,1,0,0,1
        while index<size:
            node=queue[index]
            item.append(node.val)
            count+=1
            if node.left:
                queue.append(node.left)
                next+=1
                size+=1
            if node.right:
                queue.append(node.right)
                next+=1
                size += 1
            #这一步判断必须在循环的最后
            if count==cur:
                ans.append(item[:])
                item = []
                cur,next,count=next,0,0
            index+=1
        return ans

    #根据前序遍历和中序遍历恢复二叉树
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        p=0
        n=len(preorder)
        if n==1:
            return TreeNode(preorder[0])
        if n==0:
            return None
        root=preorder[0]
        while p<n:
            if inorder[p]!=root:
                p+=1
            else:
                break
        root=TreeNode(root)

        root.left=self.buildTree(preorder[1:p+1],inorder[:p])
        root.right=self.buildTree(preorder[p+1:],inorder[p+1:])
        return root

    #113 回溯法遍历二叉树的所有路径
    def pathSum(self, root: [TreeNode], targetSum: int) -> list[list[int]]:
        ans,item=[],[]
        pSum=0
        def backtrack(node):
            nonlocal pSum
            item.append(node.val)
            pSum+=node.val

            #如果是叶子节点并且路径和等于target，把item放入ans
            if pSum==targetSum and not node.left and not node.right:
                if len(item)==0 and targetSum==0:
                    return []
                ans.append(item[:])
                return

            if node.left:
                backtrack(node.left)
                item.pop()
                pSum -= node.left.val
            if node.right:
                backtrack(node.right)
                item.pop()
                pSum -= node.right.val
        backtrack(root)
        return ans

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        temp=root.right
        root.right=root.left
        root.left=None
        p=root
        while True:
            if not p.left and not p.right:
                break
            p=p.right
        p.right=temp


if __name__ == '__main__':
    root = '[1,2,3,4,5,null,7]'
    targetSum = -5
    s=Solution()
    root=stringToTreeNode(root)
    print(s.levelOrder(root))



