class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        answer = []

        if len(digits) == 0:
            return answer

        mem = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        

        def dfs(cur, i):

            #후보 문자열을 완성했으면 answer에 추가
            if len(cur) == len(digits):
                answer.append(cur[:])
                return

            #다음 번호로 입력할 수 있는 문자들을 하나씩 집어넣어본다.
            for char in mem[digits[i]]:
                cur+=char
                dfs(cur, i+1)
                cur=cur[:-1]

        dfs(cur="", i=0)


        return answer

        