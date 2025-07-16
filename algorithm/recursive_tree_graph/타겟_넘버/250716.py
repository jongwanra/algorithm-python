"""
[문제]
https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

[문제 접근 방법]
DFS로 접근한다.
각 호출 마다, 각 요소를 뺄지, 더할지 두 가지 경우를 추가에 DFS를 호출한다.
종료조건은 depth == len(numbers)

TC: O(2^len(numbers)) .. numbers의 요소의 개수만큼 dfs가 호출되는데 각 경우가 더하거나 빼는 2가지 경우이다.
SC: O(len(numbers)) => len(numbers) 만큼 dfs가 호출되어 스택에 쌓임.

[결과]
해결 여부: ✅
소요 시간: 10:12

"""

def solution(numbers, target):
    answer = 0

    def dfs(sum: int, depth: int) -> None:
        nonlocal answer
        if len(numbers) == depth:
            if sum == target:
                answer += 1
            return
        dfs(sum + numbers[depth], depth + 1)
        dfs(sum - numbers[depth], depth + 1)

    dfs(0, 0)
    return answer


def solution_with_stack(numbers, target)->int:
    stack = [(0, 0)]
    answer = 0

    while stack:
        cur_sum, depth = stack.pop()

        if depth == len(numbers):
            if cur_sum == target:
                answer += 1
            continue

        stack.append((cur_sum + numbers[depth], depth + 1))
        stack.append((cur_sum - numbers[depth], depth + 1))

    return answer