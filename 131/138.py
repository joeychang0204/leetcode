class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution(object):
    def __init__(self):
        self.d = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        if self.d.get(head.label):
            return self.d.get(head.label)
        cur = RandomListNode(head.label)
        self.d[head.label] = cur
        cur.next = self.copyRandomList(head.next)
        cur.random = self.copyRandomList(head.random)
        #don't assign self.d here, will cause maximum recursion depth exceeded for nodes pointing to itself
        
        return cur
    def copyRandomList2(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        #first round : create copies right after each original node
        node = head
        while node:
            next = node.next
            node.next = RandomListNode(node.label)
            node.next.next = next
            node = next
        #second round : manipulate random pointers for copies
        node = head
        while node:
            if node.random:
                #node.random may not exist, else its next one should be the copied random node
                node.next.random = node.random.next
            node = node.next.next
        #third round : restore original list, get res
        dummy = copy = RandomListNode(0)
        node = head
        while node:
            copy.next = node.next
            copy = copy.next
            node.next = node.next.next
            node = node.next
        return dummy.next

head = RandomListNode(-1)
head.next = RandomListNode(1)
h = Solution().copyRandomList2(head)
#print(h.label)
#print(h.next.label)
