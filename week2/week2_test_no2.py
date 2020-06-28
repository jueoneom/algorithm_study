def solution(sentence):
    stack = []

    for s in sentence:
        last = ""
        if stack:
            last = stack[-1]

        if s == "(" or s == "[" or s == "{":
            stack.append(s)
        elif (s ==")" and last == "(") or (s == "]" and last == "[") or (s == "}" and last == "{"):
            stack.pop()
        else:
            return False

    if stack:
        return False
    return True