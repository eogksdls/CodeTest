# 입력
# 1. T개의 테스트 세트
# 2. N개의 통나무개수
# 3. 각 통나무의 높이를 나타내는 정수 (N개)
# -> 인접한 통나무의 높이차가 최소가 되는 배열 찾기

T = int(input())

tree_set = []

for i in range(T):
    N = int(input())
    tree = list(map(int, input().split(" "))) 

    if len(tree) == N:
        tree_set.append(tree)
    tree = [] # 초기화

for i in range(T):
    new = [_ for _ in range(len(tree_set[i]))]
    tree_set[i].sort(reverse=True)
    index = len(tree_set[i])//2

    if len(tree_set[i])%2 == 1: # 리스트 개수가 홀수 일 경우
        new[index] = tree_set[i][0]  # 가장 큰수가 리스트 인덱스 중앙에 위치하도록
        for j in range(index):
            new[index-(j+1)] = tree_set[i][2*j+1]
            new[index+(j+1)] = tree_set[i][2*j+2]

    else: # 리스트 개수가 짝수 일 경우
        new[index] = tree_set[i][0]  # 가장 큰수가 리스트 인덱스 중앙에 위치하도록
        for j in range(index-1):
            new[index-(j+1)] = tree_set[i][2*j+1]
            new[index+(j+1)] = tree_set[i][2*j+2]
        new[0] = tree_set[i][-1]

    List = []
    for k in range(len(new)-1):
        List.append(abs(new[k]-new[k+1]))
    List.append(abs(new[0]-new[-1]))

    print(max(List))