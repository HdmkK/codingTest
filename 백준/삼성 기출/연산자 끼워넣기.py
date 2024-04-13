import copy

N = int(input())

mem = list(map(int, input().split()))

dict = {}
tmp = list(map(int, input().split()))

#0: +, 1: -, 2: *, 3: /
for key, value in enumerate(tmp):
    dict[key] = value

max_value = -10**9
min_value = 10**9


def backtracking(n, k, dict):

    #base
    if k == N-1:
        global max_value, min_value
        max_value = max(max_value, n)
        min_value = min(min_value, n)
        return
    
    for i in range(4):
        if i == 0:
            if dict[i] > 0:
                n_dict = copy.deepcopy(dict)
                n_dict[i] -= 1
                backtracking(n + mem[k+1], k+1, n_dict)
        elif i == 1:
            if dict[i] > 0:
                n_dict = copy.deepcopy(dict)
                n_dict[i] -= 1
                backtracking(n - mem[k+1], k+1, n_dict)
        elif i == 2:
            if dict[i] > 0:
                n_dict = copy.deepcopy(dict)
                n_dict[i] -= 1
                backtracking(n * mem[k+1], k+1, n_dict)
        elif i == 3:
            if dict[i] > 0:
                n_dict = copy.deepcopy(dict)
                n_dict[i] -= 1
                
                num = 0
                if n < 0:
                    num = -int(abs(n) / mem[k+1])
                else:
                    num = int(n / mem[k+1])            
                backtracking(num, k+1, n_dict)

backtracking(mem[0], 0, dict)
print(max_value)
print(min_value)


    