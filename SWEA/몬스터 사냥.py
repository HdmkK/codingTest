D, L, N = map(int, input().split())

# total = 0
# for n in range(N):
#     total += D*(1 + (n*L)/100)
    
# print(int(total))
total = D*N + (D*L/100)*(N*(N-1)/2)
print(int(total))
    