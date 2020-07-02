rotate_num = int(input())

answers = []
for i in range(rotate_num):
    M, N, x, y = list(map(int, input().split() ))
    if x == M: x = 0
    if y == N: y = 0
    answer = -1
    for i in range(x, M*N+1, M):
        if i % N == y: 
            answer = i
            break
    answers.append(answer)
    
for ans in answers:
    print(ans)