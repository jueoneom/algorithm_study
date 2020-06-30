#refactoring 필요

brackets = input()
stack = []
brack_stack = []
total = 0

for i, bracket in enumerate(brackets):
    if bracket == "(":
        stack.append(2)
    elif bracket == "[":
        stack.append(3)
    elif not stack:
        total = 0
        break
    elif bracket == ")" and brackets[i-1] == "(" and stack[-1] == 2:
        num = stack.pop()
        for s in stack:
            num *= s
        total += num
    elif bracket == "]" and brackets[i-1] == "[" and stack[-1] == 3:
        num = stack.pop()
        for s in stack:
            num *= s
        total += num
    elif (bracket == ")" and stack[-1] == 3) or (bracket == "]" and stack[-1] == 2):
        total = 0
        break
    else:
        stack.pop()
if stack:
    total = 0
print(total)
   

    
    
