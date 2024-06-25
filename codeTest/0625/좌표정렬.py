# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

spot_list = []
n = int(input())
for i in range(n):
    spot = input().split()
    spot = list(map(int,spot))
    
    spot_list.append(spot)

# 걍 오름차순으로 정렬
# spot_list.sort()

# for val in spot_list:
#     print(val[0],val[1],end=" ")
#     print()

align = sorted(spot_list, key=lambda x: (x[0],x[1])) 
for val in align:
    print(val[0],val[1],end=" ")
    print()