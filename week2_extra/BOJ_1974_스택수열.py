rotate_num = int(input())
arr = []
num = 0
stack = [num]
answer = []
for _ in range(rotate_num):
    arr.append(int(input()))

for k in arr:   
    while k > num:
        num += 1
        stack.append(num)
        answer.append('+')       
    while stack and k < stack[-1]:
        stack.pop()
        answer.append('-')

    if stack and k == stack[-1]:
        stack.pop()
        answer.append('-')
    else:
        answer = ["NO"]
        break
for ans in answer:
    print(ans)