# W대학과 K대학 간 콘테스트
# 입력 20행 1-10행은 W대학의 참가자 점수
#           11-20행은 K대학의 참가자 점수
# 참가자 10명 중 득점이 높은 3 사람의 점수를 합산한 것을 대학의 득점으로 한다.

w_list = []
k_list = []
for i in range(10):
    w_score = int(input())
    w_list.append(w_score)
for i in range(10):
    k_score = int(input())
    k_list.append(k_score)
#---------------------------------   
w_list.sort(reverse=True) # 내림차순 : 큰 값이 앞으로 오도록
k_list.sort(reverse=True)
w_sum = 0
k_sum = 0
for i in range(3):
    w_sum += w_list[i]
    k_sum += k_list[i]

print(w_sum,k_sum,end=" ")