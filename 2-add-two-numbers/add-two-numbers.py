class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
        if not l1 and not l2 and carry == 0:
            return None
        
        total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        
        node = ListNode(total % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            total // 10
        )
        return node