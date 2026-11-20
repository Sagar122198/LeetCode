# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        curr = dummy
        x = l1
        y = l2
        carry = 0
        while x != None or y !=None or carry:
            total = carry
            if x : 
                total += x.val
                x = x.next
            if y:
                total += y.val
                y = y.next
            digit = total % 10
            carry = total //10

            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next
