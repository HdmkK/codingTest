from typing import Optional
from collections import deque

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        queue = deque()

        #데크(리스트)로 변환
        while cur:
            queue.append(cur.val)
            cur = cur.next

        #양쪽에서 pop하고 다르면->팰린드롬이 아니다(False)
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
            
        return True
