n, k = list(map(int, input().split() ))
answer = set()

for i in range(1, n + 1):
    if i * i > n : break
    elif n % i == 0: 
        answer.add(i)
        answer.add(n//i)

answer.add(n)
answer = sorted(answer)
if len(answer) < k:
    print(0)
else:
    print(answer[k-1])
