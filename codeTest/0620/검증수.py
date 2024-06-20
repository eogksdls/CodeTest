# 컴퓨터 제조회사 6자리 고유번호 매기기 
# 앞 5자리는 00000 ~ 99999 중 랜덤
# 맨 마지막 자리에는 검증수가 들어간다. 
# -> 처음 5자리에 들어가는 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

num = input()
num = num.split(" ")
int_num = list(map(int,num))

sum = 0
for i in range(len(int_num)):
    squ = int_num[i]**2
    sum += squ

# sum을 10으로 나눈 나머지
print(sum%10)

#----------------- 더 짧게
num = input()
num = num.split(" ")
int_num = list(map(int,num))

sum = 0
for i in range(len(int_num)):
    sum += int_num[i]**2

# sum을 10으로 나눈 나머지
print(sum%10)
