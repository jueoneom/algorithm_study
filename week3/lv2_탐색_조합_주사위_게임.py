from math import trunc

def solution(monster, S1, S2, S3):
    answer = -1
    total = S1 * S2 * S3
    no_monster_count = 0
    monster = set(monster)
    for s1 in range(1, S1 + 1):
        for s2 in range(1, S2 + 1):
            for s3 in range(1, S3 + 1):
                num = s1 + s2 + s3 + 1
                if not num in monster:
                    no_monster_count += 1
    return trunc(no_monster_count / total * 1000)
                