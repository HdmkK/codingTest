N = input()
answer_min = N
answer_max = N
for i in range(len(N)):
    for j in range(i+1, len(N)):
        change = N[:i] + N[j] + N[i+1:j] + N[i] + N[j+1:]
        if change[0] != "0":
            answer_min = min(answer_min, change)
        answer_max = max(answer_max, change)

print("#{} {} {}".format(test_case, answer_min, answer_max))

        


