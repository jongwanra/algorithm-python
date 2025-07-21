"""
[Problem]
https://school.programmers.co.kr/learn/courses/30/lessons/43163

가장 짧은 변환 과정 찾기?!
변할 수 없는 경우 0 return

[Plan]
BFS로 접근한다.
1. target이 words에 존재하는지 확인한다. 없으면 0 반환
2. visited 리스트를 만들고 False로 초기화
3. queue를 활용해 bfs를 돌린다.
3-1. queue에 append
3-2. queue에서 popleft()
3-3. popleft()를 한 대상으로 갈 수 있는 경우를 전부 queue에 넣는다.
3-4. 중간에 변환이 가능하다면 해당 phase를 반환한다.

[Compexity]
Time: O(N^2 * M), N: len(words), len(word)
Space: O(N), N: len(words)
"""
from collections import deque

def is_possible_transforming(word, target):
    different_count = 0
    for index in range(len(word)):
        if different_count > 1:
            break
        if word[index] is not target[index]:
            different_count += 1

    return different_count == 1


def solution(begin, target, words):
    # O(len(words))
    if not target in words:
        return 0

    word_visited = [False] * len(words)
    queue = deque([begin])
    phase = 0
    # O(N)
    while queue:
        cur_size = len(queue)
        for index in range(cur_size):
            cur_target = queue.popleft()
            if cur_target == target:
                return phase
            # O(N)
            for word_index in range(len(words)):
                if word_visited[word_index]:
                    continue
                # O(M). M -> 각 단어별 길이
                if not is_possible_transforming(cur_target, words[word_index]):
                    continue
                queue.append(words[word_index])
                word_visited[word_index] = True

        phase += 1

    return 0


def another_solution(begin:str, target:str, words)->int:
    if not target in words:
        return 0

    visited = [False] * len(words)
    queue = deque([[begin, 0]])

    while queue:
        cur_size = len(queue)
        for _ in range(cur_size):
            cur_word, cur_phase = queue.popleft()
            if cur_word == target:
                return cur_phase
            for word_index in range(len(words)):
                if visited[word_index]:
                    continue
                if not is_possible_transforming(cur_word, words[word_index]):
                    continue
                visited[word_index] = True
                queue.append([words[word_index], cur_phase + 1])
    return 0



print(another_solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))