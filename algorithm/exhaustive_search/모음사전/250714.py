# 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3

# 문제 접근 방법
# 1. 모음 사전을 전부 순열을 통해서 만든다. (A, E, I, O, U)
# 경우의 수 는 총 6^5 = 46,656

# 결과
"""
풀었지만 30분 초과

시간 복잡도 분석
N = 46,656
=> O(N log N)

공간 복잡도 분석
O(N)
"""


selected = []
result = set()
alphabets = ['', 'A', 'E', 'I', 'O', 'U']
def make_dictionary(depth:int):
    if depth == 5:
        temp = ""
        for s in selected:
            if s == '':
                continue
            temp += s
        result.add(temp)
        return

    for index in range(0, len(alphabets)):
        selected.append(alphabets[index])
        make_dictionary(depth + 1)
        selected.pop()


def solution(word):
    make_dictionary(0)

    answer = list(result)
    answer.sort()
    for index in range(len(answer)):
        if answer[index] == word:
            return index

    return 0

# print(solution('A'))
print(solution("AAAAE"))
print(solution("AAAE"))