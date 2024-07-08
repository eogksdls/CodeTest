# 문제 : N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램 작성
# 입력 : 첫째 줄에 수의 개수 => N
# 둘째 줄부터 N개의 줄에는 숫자가 주어짐

n = int(input())

numList = [int(input()) for _ in range(n)]

numList.sort(reverse=True)
for n in numList:
    print(n)
    
# 시간초과-----------------------------------------------
# pypy3로 제출하면 성공뜸
