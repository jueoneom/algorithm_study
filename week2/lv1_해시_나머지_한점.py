def solution(v_list):
    answer = []
    x_dict = {}
    y_dict = {}
    for v in v_list:
        x_dict[v[0]] = x_dict.get(v[0], 0) + 1
        y_dict[v[1]] = y_dict.get(v[1], 0) + 1
    
    answer.append(sorted(x_dict.items(),y_dict.items(), key = lambda x: x[1])[0][0])
    answer.append(sorted(y_dict.items(), key = lambda x: x[1])[0][0])
    return answer