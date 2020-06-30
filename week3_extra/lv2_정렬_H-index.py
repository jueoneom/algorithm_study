# h-index == 내림차순의 배열의 인덱스보다 인용된 값이 큰 최댓값
def solution(citations):
    citations.sort(reverse = True)
    max = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            max = i+1
    
    return max