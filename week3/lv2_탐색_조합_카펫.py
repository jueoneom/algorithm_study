'''
규칙
    1. brown가 red를 둘러쌓고 있기 때문에 red의 width, height만 알면 길이를 구할 수 있음
    1.1. brown의 개수 = (red_width + 2) * (red_height + 2) - red의 개수
    2. red의 조합은 즉 red개수의 두 약수의 곱과 같다.
    3. 카펫의 가로 길이는 언제나 가로 >= 세로이다.
    
로직: red의 조합을 찾은 후, 식에 맞는 가로, 세로 길이를 구하자.
    1. red의 조합 구하기
        1.0. for문은 i*i <= n일때 까지만 반복한다.
        1.1. red의 약수를 찾아 리스트에 넣어준다. 넣어줄 때는 brown개수를 더해주기 위해 +2를 해줌
    2. 조합에서 brown의 개수 == (red_width + 2) * (red_height + 2) - red의 개수 에 해당하는 배열을 찾으면 리턴한다.
복잡도: O(n)
'''
def search_combination(n):
    comb_arr = []
    for i in range(1, n + 1):
        if i * i > n: break
        if n % i == 0: comb_arr.append([n//i + 2, i + 2])
    return comb_arr

def solution(brown, red):
    comb_arr = search_combination(red)
    for x, y in comb_arr:    
        if brown + red == x * y:
            return [x, y]