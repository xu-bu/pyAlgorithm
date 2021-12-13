from queue import Queue

class treeNode:
    val=0
    left,right=None,None

    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left,self.right=left,right

#前序遍历
def traverse(head:treeNode):
    if head==None:
        return
    else:
        print(head.val)
        traverse(head.left)
        traverse(head.right)

#层次遍历
def visitLevel(head:treeNode,level):
    if head == None:
        return
    elif level==1:
        print(head.val)
    else:
        visitLevel(head.left,level-1)
        visitLevel(head.right,level-1)

def countHeight(head:treeNode):
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

def isFullBtree(head:treeNode):
    if pow(2,countHeight(head))-1==countNode(head):
        return True
    else:
        return False

# 使用队列把二叉树中的数据线性化。如果把二叉树的节点（包括空节点），全部放到一个队列里，会发现以下规律：
#
# A B C D E F G 0 0 0 0 0 0
#
# 规律就是前面是非空节点，而后面是空节点。如果是非完全二叉树呢，那么出现以下现象：
#
# A B 0 0 C D 0 0 E F G
def isCompleteTree(head:treeNode):
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


if __name__ == '__main__':
    head=treeNode(5)
    head.left=treeNode(3)
    head.right=treeNode(7)
    head.left.left=treeNode(2)
    head.left.right=treeNode(4)
    head.right.left=treeNode(6)
    head.right.right=treeNode(8)
    # traverse(head)
    # print(countHeight(head))
    # print(countNode(head))
    # print(isFullBtree(head))
    # for i in range(countHeight(head)):
    #     visitLevel(head,i)
    # visitLevel(head,2)
    print(isCompleteTree(head))