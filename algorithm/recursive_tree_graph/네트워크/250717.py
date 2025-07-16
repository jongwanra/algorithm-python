"""
[문제]
https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3

1<= vertax <= 200
인접행렬로 구성되어 있음.

[문제 접근 방법]
union & find를 통해서 총 네트워크 개수를 구해보자.
처음부터 끝까지 돌기 보다는 자기 자신 전까지만 돌면 원하는 네트워크 개수를 구할 수 있다.

[분석]
TC -> O(n) + O(n^2) + O(n) -> O(n^2)
SC -> unf가 n개의 개수만큼 크기의 리스트를 가지고 있다. -> O(n)

"""

def solution_with_unf(n, computers):
    unf = []

    def union(num_a:int, num_b:int)->None:
        found_num_a = find(num_a)
        found_num_b = find(num_b)
        unf[found_num_a] = found_num_b

    def find(num)->int:
        nonlocal unf

        if num == unf[num]:
            return unf[num]
        unf[num] = find(unf[num])
        return unf[num]

    # O(n)
    for index in range(n):
        unf.append(index)

    # O(n^2/2) -> O(n^2)
    for row in range(n):
        for col in range(n):
            if row == col:
                break
            if computers[row][col] == 1:
                union(row, col)

    network_set = set()
    # O(n)
    for index in range(n):
        network_set.add(find(index))

    return len(network_set)



def solution_with_dfs(n:int, computers:list)->int:
    answer = 0
    visited = [False] * n

    def handle_injective_computer(computer:int)->None:
        nonlocal visited
        nonlocal computers
        nonlocal n

        for injective_computer in range(n):
            if computer == injective_computer:
                continue
            if computers[computer][injective_computer] == 0:
                continue
            if visited[injective_computer]:
                continue
            visited[injective_computer] = True
            handle_injective_computer(injective_computer)



    for computer in range(n):
        if visited[computer]:
            continue

        answer += 1
        visited[computer] = True
        handle_injective_computer(computer)


    return answer


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution_with_dfs(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))