# 입력 : 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 주어졌을 때,
#        주어진 글자의 아스키 코드박을 출력하는 프로그램을 작성
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",\
    "q","r","s","t","u","v","w","x","y","z"]
alphaNum = [i for i in range(26)]
n = input()

if n.isdigit() == True:
    print(int(n) + 48)
else:
    if n.isupper() == True:  # 대문자일 때
        for i in range(len(alpha)):
            if n.lower() == alpha[i]:
                print(alphaNum[i]+65)
    else:  # 소문자일 때
        for i in range(len(alpha)):
            if n == alpha[i]:
                print(alphaNum[i]+97)