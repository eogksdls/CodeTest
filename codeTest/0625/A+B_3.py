# 입력 : 첫째 줄에 테스트 케이스 개수 T가 주어지고
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.(0<A, B<10)

output = []
n = int(input())

for i in range(n):
    num = input().split()
    num_int = list(map(int,num))
    
    output.append(num_int[0] + num_int[1])
    
for i in output:
    print(i)