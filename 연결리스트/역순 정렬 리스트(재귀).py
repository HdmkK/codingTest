# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node: ListNode, prev: ListNode=None):

            #head리스트를 끝까지 탐색했을 때, prev에 역순리스트가 달려있으므로
            #이를 그대로 return
            #재귀가 연쇄적으로 return하면서 prev리스트를 그대로 toss
            if not node:
                return prev
            # next = node.next
            # node.next = prev

            next, node.next = node.next, prev

            return reverse(next, node)

        return reverse(node=head)