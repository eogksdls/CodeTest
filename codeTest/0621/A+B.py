# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 작성

# arr  = input()

# arr = list(arr.split(" "))
# arr_int = list(map(int,arr))

# output = arr_int[0] + arr_int[1]

# print(output)

# 사칙연산
arr  = input()

arr = list(arr.split(" "))
arr_int = list(map(int,arr))

output = [arr_int[0]+arr_int[1],arr_int[0]-arr_int[1],arr_int[0]*arr_int[1],arr_int[0]//arr_int[1],arr_int[0]%arr_int[1] ]
for i in output:
    print(i, end="\n")