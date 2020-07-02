def solution(v_list):
    answer = []
    x_dict = {}
    y_dict = {}
    for x, y in v_list:
        if x in x_dict:
            x_dict[x] += 1
        else: x_dict[x] = 1
        
        if y in y_dict:
            y_dict[y] += 1
        else: y_dict[y] = 1
    
    answer.append(sorted(x_dict.items(), key = lambda x: x[1])[0][0])
    answer.append(sorted(y_dict.items(), key = lambda x: x[1])[0][0])
    return answer