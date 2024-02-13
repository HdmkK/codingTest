class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        #리스트(문자열)의 원소(문자)의 개수를 딕셔너리로 표현
        mem = collections.Counter(stones)

        sum = 0

        for j in jewels:
            #O(n)에 탐색
            if j in mem:
                sum += mem[j]

        return sum