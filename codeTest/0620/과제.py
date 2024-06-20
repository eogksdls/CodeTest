# 학생 명부에 각 학생별로 1-30번까지 출석번호가 부여됨
# 교수님이 내준 특별과제는 28명만이 제출했는데, 그 중 제출 안한 2명의 출석번호 구하기


# student 명부에 1-30번 학번 넣기
student = []
for i in range(30):
    student.append(i+1)

yes_list = []
for i in range(28): 
    yes_list.append(int(input()))

for s in student:
    if s not in yes_list:
        print(s,end="\n")
    