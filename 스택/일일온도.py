class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp_list = []
        stack = []
        answer = [0 for _ in range(len(temperatures))]

        for day,t in enumerate(temperatures):
            temp_list.append((day,t))

        for entry in temp_list:
            while stack and stack[-1][1] < entry[1]:
                answer[stack[-1][0]] = entry[0] - stack[-1][0]
                stack.pop()
            stack.append(entry)

        return answer
        
            