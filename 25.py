# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        block_tail = head
        block_head = head
        block_before_head = None
        new_head = head
        while True:
            for i in range(k):
                if block_tail is None:
                    return new_head
                block_tail = block_tail.next
            block_i = block_head
            block_j = block_i.next
            while block_j != block_tail:
                tmp = block_j.next
                block_j.next = block_i
                block_i = block_j
                block_j = tmp
            block_head.next = block_tail
            if block_before_head == None:
                new_head = block_i
            else:
                block_before_head.next = block_i
            block_before_head = block_head
            block_head = block_tail
