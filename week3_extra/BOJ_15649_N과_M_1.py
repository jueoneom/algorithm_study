'''
[문제] 
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오
(1<=M<=N<=8)
경우의 수 알고리즘
[아이디어]
is_used를 통해 해당 숫자가 쓰였는지 확인하기
arr 배열에 한 수열 배치 넣기
1부터 k+1 (n) 까지 반복한다. (ex> k = 3, m = 3 )
    0) is_used[i]가 False일 경우에만 수행한다.
    1) 먼저 첫 i칸에 해당하는 is_used[i]를 사용한다는 표시를 하고 (0 0 0)(F T F F)
    2) arr의 n 인덱스에 i값을 넣는다. (i값은 경우의 숫자인 셈) (i, 0, 0) (F T F F)
    2) 나머지 위치에 경우의 수를 배치하기 위해 n+1로 재귀를 돈다. (i, i, 0) (F )
    3) 리턴하고나서는 is_used[i]를 False처리해줌
'''

# answer = []
def backTracking(n):
    if m == n:
        # answer.append(arr)
        # print(arr)
        for i in arr:
            print(i , end = " ")
        print("")
        return 
    for i in range(1, k+1):
        if not is_used[i]:
            is_used[i] = True
            arr[n] = i
            backTracking(n+1)
            is_used[i] = False



k, m = list(map(int, input().split()))
arr = [0] * m
is_used = [False] * (k + 1)

backTracking(0)