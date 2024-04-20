T = int(input())

for test_case in range(1, T+1):
    
    answer = 10**9
    X, Y, Z = map(int, input().split())
    
    ret1 = abs((2*Y-Z)-X)
    ret2 = abs(((X+Z)/2)-Y)
    ret3 = abs((2*Y-X)-Z)
    
    ret = min(ret1, ret2, ret3)
    print("#{} {:.1f}".format(test_case, ret))
    
    
    # if Y-X == Z-Y:
    #     answer = 0
    # else:
    #     ret = (2*Y)-Z
    #     # if abs(answer) > abs(ret-X):
    #     #     answer = ret-X
    #     answer = min(answer, abs(ret-X))
        
    #     ret = float(format((X+Z)/2, ".1f"))
    #     # if abs(answer) > abs(float(format(ret-Y, ".1f"))):
    #     #     answer = float(format(ret-Y, ".1f"))
    #     answer = min(answer, abs(ret-Y))
        
    #     ret = (2*Y)-X
    #     # if abs(answer) > abs(ret-Z):
    #     #     answer = ret-Z
    #     answer = min(answer, abs(ret-Z))
        
        
        
    
    