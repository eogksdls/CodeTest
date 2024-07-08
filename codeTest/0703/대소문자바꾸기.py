# 문제 :  영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 -> 소문자로, 소문자는 대문자로 바꾸어 출력하기


str = list(input())

for s in str:
    if s.islower()==True:
        s1 = s.upper()
    else:
        s1 = s.lower()
    
    print(s1,end="")
