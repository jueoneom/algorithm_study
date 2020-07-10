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

'''
규칙
    1. 직사각형 좌표는 동일한 x와 y 좌표가 두개씩 있어야한다.
    2. 입력값은 [x,y] 리스트
    3. 출력값은 [x,y]
로직
    1. dictionary를 통해 동일한 x, y값이 몇갠지 확인한다. (collections Counter 클래스 사용예정)
    2. x, y가 각각 1개인 key값을 리턴하도록 하자
'''

from collections import Counter
def solution(v_list):
    x_list = [x for x, _ in v_list]
    y_list = [y for _, y in v_list]
    
    x_list = sorted(Counter(x_list).items(), key = lambda x: x[1])
    y_list = sorted(Counter(y_list).items(), key = lambda x: x[1])
    
    return [x_list[0][0], y_list[0][0]]

