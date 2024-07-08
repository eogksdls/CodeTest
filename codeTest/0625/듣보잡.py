
first = list(input().split())
N = int(first[0])
M = int(first[1])

no_hear = [_ for _ in range(N)]
no_see = [_ for _ in range(M)]

for i in range(N):    # for문이 한 번 돌때 1ms
    no_hear[i] = input()
for i in range(M):
    no_see[i] = input()

cnt = 0
no_hear_see = []
for h in no_hear:
    if h in no_see:
        no_hear_see.append(h)
        cnt += 1

no_hear_see.sort() # 사전순으로 정렬
# 출력
print(cnt)
answer = ""
for p in no_hear_see:
    answer += str(p) + '\n'
print(answer)


# 시간초과

first = list(input().split())
N = int(first[0])
M = int(first[1])

no_hear = [input() for _ in range(N)]
no_see = [input() for _ in range(M)]


no_hear_see = []
for h in no_hear:
    if h in no_see:
        no_hear_see.append(h)

no_hear_see.sort()

print(len(no_hear_see))
for p in no_hear_see:
    print(p)
