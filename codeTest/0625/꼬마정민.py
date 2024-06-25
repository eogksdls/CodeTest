# A + B + C 계산
# 입력 : 첫 번째 줄에 A,B,C( 1<= A,B,C <= 10^12)가 공백을 사이에 두고 주어짐

n = input().split() # 공백을 기준으로 split하여 리스트에 넣어줌

n_int = list(map(int,n))

sum = 0
for i in n_int:
    sum += i
print(sum)