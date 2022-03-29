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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNum(head):
            ret=0
            p=head
            while p:
                ret*=10
                ret+=p.val
            return ret
        num1=getNum(l1)
        num2=getNum(l2)
        newNum=list(num1+num2)
        head=ListNode()
        p=head
        for each in newNum:
            node=ListNode(each)
            p.next=node
            p=p.next
        p.next=None
        return head.next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1,p2=headA,headB
        while p1!=p2:
            if p1==p2:
                return p1
            if not p1.next:
                p1=headA
            else:
                p1=p1.next
            if not p2.next:
                p2=headB
            else:
                p2=p2.next
            if p1 == headA and p2 == headB:
                return None

if __name__ == '__main__':
    head = [4,2,1,3]

    s=Solution()
    head=s.createList(head)


    s.sortList(head).traverse()


