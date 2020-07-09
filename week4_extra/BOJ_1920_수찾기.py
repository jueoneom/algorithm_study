def binary_search(numbers, k_numbers):
    numbers.sort()
    for k in k_numbers:
        start = 0
        end = len(numbers) - 1
        result = 0
        while start <= end: 
            mid = (start + end) // 2
            if numbers[mid] == k:
                result = 1
                break
            elif numbers[mid] > k:
                end = mid - 1
            elif numbers[mid] < k:
                start = mid + 1
        print(result)
    return 0


n = int(input())
n_numbers = list(map(int, input().split()))
m = int(input())
m_numbers = list(map(int, input().split()))

binary_search(n_numbers, m_numbers)

