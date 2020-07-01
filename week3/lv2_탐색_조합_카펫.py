#조합 구하기
def combination(n):
    nums = []
    for i in range(1, n + 1):
        if i * i > n: break
        if n % i == 0:
            nums.append((i, int(n/i)))
    return nums
            
def solution(brown, red):
    answer = []
    red_comb = combination(red)
    for x, y in red_comb:
        if (x + 2) * (y + 2) - red == brown:
            return [y + 2, x + 2]
    