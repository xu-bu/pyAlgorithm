class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def tailInsert(self,val):
        p=self
        while p.next!=None:
            p=p.next
        node=ListNode(val)
        p.next=node

    def traverse(self):
        p = self
        while p != None:
            print(p.val,end="->")
            p = p.next

class Solution:
    def createList(self,nums):
        head=ListNode(nums[0])
        for i in range(1,len(nums)):
            head.tailInsert(nums[i])
        return head


if __name__ == '__main__':
    head = [4,2,1,3]

    s=Solution()
    head=s.createList(head)


    s.sortList(head).traverse()


