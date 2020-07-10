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


    '''
규칙
    1. names 차례대로 물건을 싣는다. max_weight까지만 싣고 떠나야함
    2. 트럭은 총 몇대가 필요한가? 
로직
    1. specs를 dict로 바꾸고
    2. names로 반복문을 돌며 누적 무게를 구한다. 
    3. max_weight 보다 누적 무게가 커질 경우 answer +=1, 누적 무게를 비우고 다시 더한다.
'''
def solution(max_weight, specs, products):
    answer = 1
    specs = dict(specs)
    cumulative_weight = 0
    for product in products:
        if cumulative_weight + int(specs[product]) > max_weight:
            cumulative_weight = 0
            answer += 1
        cumulative_weight += int(specs[product])
    
    return answer