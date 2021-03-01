class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(4, None)
b = a
b.val = 1
print(a.val)
