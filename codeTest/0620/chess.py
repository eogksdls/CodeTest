# 체스 피스 세트 1,1,2,2,2,8 총 16개!

# 입력 조건 : 동혁이가 찾은 킹,퀸,룩,비숍,나이트,폰 개수
# 출력 : 입력값에서 주어진 순서대로 몇 개의 피스를 더하거나 뺴야되는지 출력

# 입력 (리스트 형태로...)

def solution(arr):
    chess = [1,1,2,2,2,8]
    output = []
    
    arr = list(arr.split(" "))
    int_arr = list(map(int,arr))

    for i in range(len(int_arr)):
        if chess[i] == int_arr[i]:
            output.append(0)
        elif chess[i] > int_arr[i] or chess[i] < int_arr[i]:
            output.append(chess[i]-int_arr[i])
    
    # 출력
    # print("출력값 : ",end=" ")
    for j in output:
        print(j,end=" ")

arr = input()
solution(arr)

#------------------짧게!!!

arr = input()
arr = arr.split(" ")
int_arr = list(map(int,arr))

chess = [1,1,2,2,2,8]
output = []

for i in range(len(int_arr)):
    if chess[i] == int_arr[i]:
        output.append(0)
    elif (chess[i] > int_arr[i]) or (chess[i] < int_arr[i]):
        output.append(chess[i]-int_arr[i])

# 출력
# print("출력값 : ",end=" ")
for j in output:
    print(j,end=" ")