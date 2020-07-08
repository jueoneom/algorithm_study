
def backtracking(cur, k):
    if cur == m:
        for i in arr:
            print(i , end = " ")
        print("")
        return
    
    for i in range(1, n+1):
        if not is_used[i] and k < i:
            is_used[i] = True
            arr[cur] = i
            backtracking(cur + 1, i)
            is_used[i] = False
        

n, m = list(map(int, input().split()))
arr = [0] * m
is_used = [False] * (n + 1)
backtracking(0, 0)