class Solution:
    
    mem = {}
    def climbStairs(self, n: int) -> int:

        if n == 1:
            self.mem[1] = 1
            return self.mem[1]
        elif n == 2:
            self.mem[2] = 2
            return self.mem[2]
       
        if n-1 not in self.mem:
            self.mem[n-1] = self.climbStairs(n-1)
        if n-2 not in self.mem:
            self.mem[n-2] = self.climbStairs(n-2)

        return self.mem[n-1] + self.mem[n-2]