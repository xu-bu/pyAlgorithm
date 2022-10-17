from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def tailInsert(self, val):
        p = self
        while p.next != None:
            p = p.next
        node = ListNode(val)
        p.next = node

    def traverse(self):
        p = self
        while p != None:
            print(p.val, end="->")
            p = p.next


def createLinkedList(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = head.next
        newHead = self.reverseList(head.next)
        tail.next = head
        return newHead

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead,evenHead=ListNode(),ListNode()
        p=oddHead
        q=evenHead
        flag=True
        while(head):
            if(flag):
                p.next=head
                p=p.next
                flag=False
            else:
                q.next=head
                q=q.next
                flag = True
            head=head.next
        p.next=evenHead.next
        q.next=None
        return oddHead.next

if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    head = createLinkedList(head)

    s = Solution()

    head=s.oddEvenList(head)
    head.traverse()
