# 엘리스 토끼는 목표량을 정해 수학 문제를 열심히 풉니다. 목표량은 정수입니다.

# 내일 풀 수학 문제의 개수는 오늘 푼 문제 개수의 수와 숫자의 구성이 같으면서, 오늘 푼 문제 개수의 수보다 큰 수 중 가장 작은 수입니다.

# 예를 들어, 오늘 67문제를 풀었으면 다음 날 76문제를 풉니다.

# 오늘 푼 문제의 개수를 줬을 때 다음날 풀 문제의 개수를 출력하는 프로그램을 작성하세요.

import itertools

quiz = input()  # 최대 6자리 수

#----------------------------------------------------------------
# 입력한 숫자를 가지고 생성할 수 있는 모든 순열 생성
all_list = itertools.permutations(list(quiz))
# str 인 순열을 정수로 변환하고, 중복을 제거하여 집합에 추가
unique = set(int(''.join(p)) for p in all_list)
# print(unique)
# 처음에 입력한 숫자보다 작은 값은 제거
unique = [u for u in unique if u > int(quiz)]
# 정렬하여 가장 작은 값 찾기
unique.sort()
# 결과출력
print(unique[0])



