class Solution:
    def fib(self, n: int) -> int:
        
        #타뷸레이션

        mem = {}

        mem[0] = 0
        mem[1] = 1

        for i in range(2, n+1):
            mem[i] = mem[i-1] + mem[i-2]

        return mem[n]

        

        
        