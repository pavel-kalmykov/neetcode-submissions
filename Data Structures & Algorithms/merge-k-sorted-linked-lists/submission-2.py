# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l, r) -> ListNode:
            sentinel = ListNode(None)
            curr = sentinel

            while l and r:
                if l.val <= r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
                curr = curr.next

            curr.next = l or r
            
            return sentinel.next

        def divide(_lists, l, r) -> Optional[ListNode]:
            if l > r:
                return None
            if l == r:
                return _lists[l]

            mid = l + (r - l) // 2
            l = divide(_lists, l, mid)
            r = divide(_lists, mid + 1, r)

            return merge(l, r)

        return divide(lists, 0, len(lists) - 1)
