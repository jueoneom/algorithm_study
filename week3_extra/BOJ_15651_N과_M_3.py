
def backtracking(cur):
    if cur == m:
        for i in arr:
            print(i , end = " ")
        print("")
        return
    
    for i in range(1, n+1):
        arr[cur] = i
        backtracking(cur + 1)
            

n, m = list(map(int, input().split()))
arr = [0] * m
backtracking(0)