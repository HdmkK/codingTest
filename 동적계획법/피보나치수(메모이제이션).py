class Solution:
    mem = {}

    def fib(self, n: int) -> int:
        
       #메모이제이션

       #base
        if n <= 1:
            return n

        if n in self.mem:
            return self.mem[n]
        else:
            self.mem[n] = self.fib(n-1) + self.fib(n-2)
            return self.mem[n]
