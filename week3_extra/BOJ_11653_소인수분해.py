rotate_num = int(input())

answer = []

for i in range(2, (rotate_num+1)):

    if i * i > rotate_num:
        if rotate_num > 1:
            answer.append(int(rotate_num))
        break
    while rotate_num % i == 0:
        answer.append(i)
        rotate_num /= i

for ans in answer:
    print(ans)
