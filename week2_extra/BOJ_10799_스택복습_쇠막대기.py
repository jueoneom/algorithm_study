brackets = input()
stack = []
answer = 0
for i, bracket in enumerate(brackets):
    if bracket == "(":
        stack.append(bracket)
    elif bracket == ")" and brackets[i-1] == "(":
        stack.pop()
        answer += len(stack)
    else:
        stack.pop()
        answer += 1
print(answer)