# 입력 : 각 테스트케이스는 정수 n으로 시작하며 주어지는 단어의 개수를 뜻함
# 다음 각 n줄은 길이가 최대 20인 단어가 주어지며, 대소문자 구분을 없앴을 때 똑같은 단어는 주어지지 않음

# 마지막 입력은 0이 주어짐
final = []

while True:
    n = int(input())
    if n == 0:
        break
    elif (2 <= n <= 1000):
        word = []
        for i in range(n):
            w = input()
            word.append(w)
            
        # 모두 소문자로 변환했을 때, 오름차순으로 정렬
        align = sorted(word, key=lambda x: x.lower())
        # print(align)
        final.append(align[0]) # 가장 앞서는 단어만 append
    

# 출력
for w in final:
    print(w)
