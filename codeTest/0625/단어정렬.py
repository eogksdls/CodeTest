# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램

# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

word = []
cnt = 0

n = int(input())  # 단어 개수
while cnt<n:
    w = input()
    if len(w) <= 50:
        word.append(w)
        cnt += 1

word = list(set(word)) # 중복되는 단어 1개만 남기고 제거
# 문자 길이가 짧은 것부터, 길이가 같으면 사전 순으로
align = sorted(word, key=lambda x: (len(x), x))

for w in align:
    print(w)

