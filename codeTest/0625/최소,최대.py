# N개의 정수가 주어진다. 
# 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

n = int(input())

num = input().split()
num_list = []

if len(num) == n:  # n개보다 많은 수가 입력되면 오류
    num = list(map(int,num))

    for i in num:
        num_list.append(i)

print(min(num_list),max(num_list), end=" ")


# 보완