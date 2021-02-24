# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ordered_list = []
        minimum = 300000
        min_index = 0
        lists = list(filter(None, lists))

        while(len(lists) != 0):

            minimum = 300000

            for index in range(0, len(lists)):

                if(lists[index].val < minimum):
                    minimum = lists[index].val
                    min_index = index
            ordered_list.append(minimum)
            if(lists[min_index].next == None):
                lists.remove(lists[min_index])
            else:
                lists[min_index] = lists[min_index].next
        li = None
        for i in reversed(ordered_list):
            a = ListNode(i, li)
            li = a

        return li
