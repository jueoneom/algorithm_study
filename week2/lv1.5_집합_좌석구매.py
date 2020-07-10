def solution(seat):
    return len(set(map(tuple,seat)))


'''
규칙
    1. 성공한 사람의 수 == 중복되지 않은 seat의 개수
로직
    1. seat을 집합으로 만들어 중복을 없앤 후, 개수를 세서 리턴한다.
    2. map 사용하는 걸 잊지말자!!!!
'''
def solution(seats):
    return len(set(map(tuple, seats)))