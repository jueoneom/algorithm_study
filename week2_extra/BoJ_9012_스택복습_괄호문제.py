
rotate_num = int(input())
stack = []
answer = []
for _ in range(rotate_num):
    brackets = input()
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif stack and stack[-1] == "(" :
            stack.pop()
        else:
            stack.append(-1)
            break
    if stack:
        answer.append("NO")
    else:
        answer.append("YES")
    stack.clear()

for ans in answer:
    print(ans)
