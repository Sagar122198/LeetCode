# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#### Will not pass all the test cases #### 
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        x = l1
        y = l2
        num1 = 0
        num2 = 0
        while x != None:
            num1 = num1 * 10 + x.val
            x = x.next
        while y != None:
            num2 = num2 * 10 + y.val
            y = y.next
        num1 = int(str(num1)[::-1])
        num2 = int(str(num2)[::-1])
        result = num1 + num2 
        dummy = ListNode()
        curr = dummy

        while result > 0:
            digit = result % 10

            curr.next = ListNode(digit)
            curr = curr.next

            result //= 10
        return dummy.next
