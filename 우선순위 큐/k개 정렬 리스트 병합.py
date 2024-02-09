# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        answer = ListNode()

        for cur in lists:
            while cur != None:
                heapq.heappush(heap, cur.val)
                cur = cur.next
        
        cur_answer = answer

        for _ in range(len(heap)):
            val = heapq.heappop(heap)
            cur_answer.next = ListNode(val)
            cur_answer = cur_answer.next

        return answer.next
