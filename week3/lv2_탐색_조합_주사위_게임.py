'''
idea: 완탐 문제. s1, s2, s3의 조합을 구한 후, 합이 monster이 아닐 경우만을 찾자.
복잡도: O(S1 * S2 * S3) O(n^3)
'''
from math import trunc

def solution(monster, S1, S2, S3):
    total = S1 * S2 * S3
    cnt = 0
    monster = set(monster)
    
    for s1 in range(1, S1 + 1):
        for s2 in range(1, S2 + 1):
            for s3 in range(1, S3 + 1):
                s_sum = s1 + s2 + s3 + 1
                if not s_sum in monster:
                    cnt += 1
    
    return trunc(cnt / total * 1000)