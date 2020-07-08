'''
규칙
    1. 정확히 신청한 금액을 지원해주어야 한다.
    2. 리턴값은 총 지원한 부서
    3. 최대한 많은 부서의 물품을 구매해준다 == 요청 금액이 작은 부서부터 지원
로직
    1. d를 작은 수를 기준으로 정렬한다.
    2. 정렬한 d를 기준으로 budget을 소비한다. budget<d[i]이면 종료
복잡도
    1. 정렬하는 데 O(n)
    2. 정렬된 item과 budget 비교, 탐색하는 데 O(n)
'''
def solution(d, budget):
    answer = 0
    for item in sorted(d):
        if budget < item: break
        budget -= item
        answer += 1
    
    return answer