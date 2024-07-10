# 8 3
# 1 7 6 8 1 6 4 5
# 1 5 3
# 2 6 2
# 4 8 3

# 첫째줄에 배열의 개수, 테스트 세트
# 배열이 주어지고
# 범위 (1,5) 중 오름차순으로 정렬했을 시 3번째인 숫자 print

set = input().split(" ")
n = int(set[0])
m = int(set[1])
arr = list(map(int,input().split(" ")))
if len(arr) == n:
    answer = []
    for i in range(m):
        test = input().split(" ") # test = [1,5,3]
        start = int(test[0])
        end = int(test[1])
        index = int(test[2])-1
        new = arr[start-1:end]
        new.sort()
        answer.append(new[index])

for a in answer:
    print(a)
