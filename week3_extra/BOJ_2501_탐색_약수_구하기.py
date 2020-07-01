n, k = list(map(int, input().split() ))
answer = []

for i in range(1, n + 1):
    if i * i > n : break
    elif n % i == 0: answer.append(i)

for i in range(len(answer)-1, 0, -1):
    if answer[i] * answer[i] == n: continue
    answer.append(n // answer[i])
answer.append(n)
if len(answer) < k:
    print(0)
else:
    print(answer[k-1])
