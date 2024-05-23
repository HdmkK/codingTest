    A, B, C, D = map(int, input().split())

    answer = 0

    if B < C or D < A:
        answer = 0
    else:
        a = max(A, C)
        b = min(B, D)
        answer = b-a

    string += "#{} {}\n".format(test_case, answer)
print(string)