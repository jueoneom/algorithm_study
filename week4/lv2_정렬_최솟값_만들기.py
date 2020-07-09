'''
규칙
    1. 배열의 각각의 원소를 곱해 더한 값이 최소가 되도록 하라.
    1.1. == A는 최소값 정렬, B는 최댓값 정렬을 한 후, 각 인덱스에 해당하는 값을 곱하여 더하면 최소가 된다.
    
로직
    1. 배열 A는 최솟값 정렬, 배열 B는 최댓값 정렬을 한다.
    2. for문을 돌려서 각 인덱스에 해당하는 값을 곱하여 누적해 더한다.
    
복잡도
    1. A, B를 정렬하는데 드는 시간 O(2n)
    2. A와 B의 원소를 탐색하는데 드는 시간 O(n)
    ==> O(3n)
'''
def solution(A,B):
    answer = 0
    
    for a, b in zip(sorted(A, key = lambda x: x), sorted(B, key = lambda x: -x)):
        answer += a*b
    
    return answer