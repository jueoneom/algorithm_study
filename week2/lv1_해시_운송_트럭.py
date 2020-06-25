def solution(max_weight, specs, names):
    answer = 0
    spec_dict = dict(specs)
    sum = 0
    for name in names:
        product = int(spec_dict[name])
        if sum + product > max_weight:
            sum = product
            answer += 1
        else: sum += product
    if sum > 0:
        answer += 1
    return answer