class Solution:
    def isValid(self, s: str) -> bool:
        
        mem = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for c in s:

            if c in mem:
                if stack and stack[-1] == mem[c]:
                    stack.pop()
                    continue
            stack.append(c)

        if not stack:
            return True
        else:
            return False