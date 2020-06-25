'''
문제
문장이 주어졌을 때, 가장 많이 등장하려는 단어를 구하려 합니다.
'''

#1 dictionary를 사용한 풀이
def solution(sentence):
    words = sentence.split(" ")
    my_counter = {}
    for word in words:
        my_counter[word] = my_counter.get(word, 0) + 1
    
    return sorted(my_counter.items(), key = lambda x: -x[1])[0][0]
    
#2 collections Counter 클래스를 이용한 풀이

from collections import Counter
def solution(sentence):
    sentence = sentence.split(" ")
    my_dict = Counter(sentence)
    return sorted(my_dict.items(), key = lambda x: -x[1])[0][0]