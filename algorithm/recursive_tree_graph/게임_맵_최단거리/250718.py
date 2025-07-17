"""
[문제]
https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

최단 거리 구하기 문제 -> BFS
n x m 맵 크기 (1 <= n,m <= 100)
초기 위치: (1, 1)
목적지: (n, m)
상대팀 진영에 못 도착하는 경우도 있다. -> -1 return

0 = 벽
1 = 벽 없음

[문제 접근 방법]
BFS를 사용한다.

"""

from collections import deque


def solution(maps):
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]
    dest_row, dest_col = [len(maps) - 1, len(maps[0]) - 1]

    # 이거 쉽게 만드는 방법 찾기
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    queue = deque()
    visited[0][0] = True
    queue.append([0, 0])

    while queue:
        cur_size = len(queue)
        for cur_index in range(cur_size):
            cur_row, cur_col = queue.popleft()

            for index in range(4):
                n_row = cur_row + d_row[index]
                n_col = cur_col + d_col[index]

                if n_row < 0 or n_col < 0 or n_row > dest_row or n_col > dest_col:
                    continue
                if maps[n_row][n_col] == 0:
                    continue
                if visited[n_row][n_col]:
                    continue

                visited[n_row][n_col] = True
                maps[n_row][n_col] = maps[cur_row][cur_col] + 1

                # 사전에 찾게 되면 바로 return
                if n_row == dest_row and n_col == dest_col:
                    return maps[n_row][n_col]

                queue.append([n_row, n_col])

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
