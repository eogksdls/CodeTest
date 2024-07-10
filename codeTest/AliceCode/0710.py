# 문자열 압축 해제 후 문자열 전체 길이를 출력

# K(Q) K는 한 자리 정수, Q는 반복되는 문자열로 0자리 이상이다.
# K(Q)는 문자열 Q가 K번 반복된다는 말


str = list(input())

index_left = []  # "("가 나오는 인덱스
index_right = [] # ")"가 나오는 인덱스
for i, s in enumerate(str):
    if s == "(":
        index_left.append(i)
    elif s == ")":
        index_right.append(i)

index_left.sort(reverse=True) # 내림차순 정렬
intIndex = [i-1 for i in index_left] # '('앞의 index니까 1씩 빼주기

length = 0
if index_right[0] - index_left[0] == 2:  # ( ) 사이에 문자열 길이가 1일 경우
    for i in range(len(index_left)-1):
        if i == 0:
            length = int(str[intIndex[i]])*1
            length += (intIndex[i]-index_left[i+1]-1)
        else:
            length = int(str[intIndex[i]])*length
            length += (intIndex[i]-index_left[i+1]-1)
            
    length += intIndex[-1]
    print(length) #문자열 길이나옴
    
else:
    for i in range(len(index_left)-1):
        if i == 0:
            length = int(str[intIndex[i]])*(index_right[0]-index_left[0]-1)
            length += (intIndex[i]-index_left[i+1]-1)
        else:
            length = int(str[intIndex[i]])*length
            length += (intIndex[i]-index_left[i+1]-1)
    length += intIndex[-1]
    print(length) #문자열 길이나옴




