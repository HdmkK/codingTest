import math


def cal_score(d):
    
    if 0 <= d <= 400:
        return 10
    elif 400 < d <= 1600:
        return 9
    elif 1600 < d <= 3600:
        return 8
    elif 3600 < d <= 6400:
        return 7
    elif 6400 < d <= 10000:
        return 6
    elif 10000 < d <= 14400:
        return 5
    elif 14400 < d <= 19600:
        return 4
    elif 19600 < d <= 25600:
        return 3
    elif 25600 < d <= 32400:
        return 2
    elif 32400 < d <= 40000:
        return 1
    else:
        return 0
        
    
    

N = int(input())

darts = []
for _ in range(N):
    x, y = map(int, input().split())
    darts.append((x, y))
    

total_score = 0
for x, y in darts:
    
    d = x**2 + y**2
    total_score += cal_score(d)

string += "#{} {}\n".format(test_case, total_score)
print(string)
    