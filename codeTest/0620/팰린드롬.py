# 입력값 : 알파벳 소문자
# 출력값 : 0 또는 1

# 팰린드롬 : 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어
# 입력 단어가 팰린드롬인지 아닌지 확인하는 프로그램 작성

word = input()

# len(word)가 홀수면 단어 가운데 index를 기점으로 양쪽 스펠링이 동일해야함
if len(word)%2 == 1:
    # 단어의 중앙 index 값 (index는 0부터 시작하니까 주의!)
    index = len(word)//2
    cnt = 0
    for i in range(index):
        if word[index-(i+1)] == word[index+(i+1)] :
            cnt += 1 # 대칭이면 cnt가 세지는 것을 이용 
    
    # cnt수가 index의 값과 동일해야 1을 반환하도록
    if cnt == index:
        answer = 1
    else:
        answer = 0    
    print(answer)
            
# len(word)가 짝수면... 대칭
elif len(word)%2 == 0:
    index = len(word)//2
    cnt = 0
    for i in range(index):
        if word[index-(i+1)] == word[index+i]:
            cnt += 1

    # cnt수가 index의 값과 동일해야 1을 반환하도록
    if cnt == index:
        answer = 1
    else:
        answer = 0    
    print(answer)
    

# 단어 가운데에서 대칭이 아니더라도, 마지막에 대칭이면 1을 반환하네..