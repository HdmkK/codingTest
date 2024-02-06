# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        

        dummy = ListNode()
        dummy.next = head

        #이전 노드
        prev = dummy
        cur = head

        #역순 시작 노드까지 skip
        for _ in range(left-1):
            prev = cur
            cur = cur.next

        start = prev.next

        #right - left만큼 뒤집기
        for _ in range(right - left):
            

            # prev.next = start.next
            # start.next.next = cur
            # start.next = start.next.next
            prev.next, start.next.next, start.next = start.next, cur, start.next.next

            cur = prev.next

            

        return dummy.next

        