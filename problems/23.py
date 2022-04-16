# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def node_compare(node1, node2):
    if node1.val > node2.val:
        return 1
    if node1.val == node2.val:
        return 0
    return -1

class Heap(object):
    def __init__(self):
        self.len = 0
        self.heap = []

    def push(self, node):
        if node is None:
            return

        self.heap.append(node)
        self.len += 1
        self.up(self.len-1)

    def up(self, now):
        if now == 0:
            return
        father = (now-1)/2
        if node_compare(self.heap[now], self.heap[father]) < 0:
            tmp = self.heap[now]
            self.heap[now] = self.heap[father]
            self.heap[father] = tmp
            self.up(father)

    def down(self, now):
        if now * 2 + 1 >= self.len:
            return
        son = now * 2 + 1
        if now * 2 + 2 < self.len and node_compare(self.heap[son], self.heap[now * 2 + 2]) > 0:
            son = now * 2 + 2
        if node_compare(self.heap[now], self.heap[son]) > 0:
            tmp = self.heap[now]
            self.heap[now] = self.heap[son]
            self.heap[son] = tmp
            self.down(son)

    def pop(self):
        if self.len == 0:
            return None
        ret = self.heap[0]
        self.heap[0] = self.heap[self.len-1]
        self.len -= 1
        self.heap.pop()
        self.down(0)
        return ret


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        now = None
        heap = Heap()
        for node in lists:
            heap.push(node)
        while True:
            min_node = heap.pop()
            if min_node is None:
                return head
            if head is None:
                head = ListNode(min_node.val)
            elif now is None:
                head.next = ListNode(min_node.val)
                now = head.next
            else:
                now.next = ListNode(min_node.val)
                now = now.next
            if min_node.next is not None:
                heap.push(min_node.next)
