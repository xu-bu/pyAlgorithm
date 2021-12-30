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
    def reverse(self,head:ListNode)->ListNode:
        if head==None or head.next==None:
            return head
        kn=self.reverse(head.next)
        head.next.next=head
        head.next=None
        return kn

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #初始化哑节点，最后返回newHead.next
        newHead=ListNode(0)
        p=newHead
        carry=0
        while l1!=None and l2!=None:
            sum=l1.val+l2.val
            val = sum % 10
            p.next = ListNode(val + carry)
            p=p.next
            if sum>=10:
                carry=1
            else:
                carry=0
            l1=l1.next
            l2=l2.next
        while l1!=None:
            p.next=ListNode(l1.val)
            p=p.next
        while l2!=None:
            p.next=ListNode(l2.val)
            p=p.next
        p.next=None
        return newHead.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next==None:
            return None
        ne=head
        for i in range(n):
            ne=ne.next
        if ne==None:
            return head.next
        pre=head
        cur=pre.next
        ne=ne.next
        while ne!=None:
            ne=ne.next
            pre=pre.next
            cur=cur.next
        pre.next=cur.next
        return head

    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        else:
            newHead=head.next
            head.next=newHead.next
            newHead.next=head
            def subSwapPairs(pre:ListNode):
                if pre==None or pre.next==None or pre.next.next==None:
                    return
                else:
                    fir=pre.next
                    sec= fir.next
                    pre.next=sec
                    fir.next=sec.next
                    sec.next=fir
                    subSwapPairs(fir)
            subSwapPairs(head)
            return newHead

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k==0:
            return head
        length=2
        #the last 2 nodes is p,q
        p=head
        q=head.next
        while q.next!=None:
            p=p.next
            q=q.next
            length+=1
        if k>=length:
            return self.rotateRight(head,k-length)
        q.next=head
        p.next=None
        return self.rotateRight(q,k-1)




if __name__ == '__main__':
    head=ListNode(9)
    head.tailInsert(9)
    head.tailInsert(9)
    head.tailInsert(9)
    head.tailInsert(9)
    head.tailInsert(9)
    head.tailInsert(9)

    l2=ListNode(2)
    l2.tailInsert(5)
    l2.tailInsert(3)
    l2.tailInsert(4)
    l2.tailInsert(6)

    s=Solution()
    # newHead=s.addTwoNumbers(head,l2)
    # newHead=s.swapPairs(l2)
    l2.traverse()
    print()
    l2=s.rotateRight(l2,1)
    l2.traverse()


