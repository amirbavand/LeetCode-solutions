# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        ordered_list = []
        minimum = 300000
        min_index = 0
        min_el = None
        lists = list(filter(None, lists))

        while(len(lists) != 0):

            minimum = 300000

            for index, lem in range(0, len(lists)):

                if(lists[index].val < minimum):
                    minimum = lem.val
                    min_index = index
                    min_el = lem
            ordered_list.append(minimum)

            lists[min_index] = min_el.next
        li = None
        for i in reversed(ordered_list):
            a = ListNode(i, li)
            li = a

        return li


b = [None]
a = Solution()
print(a.mergeKLists(b))
