# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur_node = head
        dummy = ListNode()

        #리스트를 차례로 읽어서 항상 dummy노드 다음에 끼워넣기 
        while cur_node:
            next = cur_node.next
            dummy.next, cur_node.next = cur_node, dummy.next
            cur_node = next

        return dummy.next