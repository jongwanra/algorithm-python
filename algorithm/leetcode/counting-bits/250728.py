"""
[Problem]
https://leetcode.com/problems/counting-bits/description/

[Brain Storm]
ans[i] = i -> binary -> 1의 개수

[Plan]
1.
"""
from typing import List

class Solution:
    """
    [Plan]
    Brute Force
    1. n + 1 만큼 for-loop로 순회한다.
        1-1. num을 binary로 변환한다.
        1-2. binary num을 for-loop로 순회한다.
            1-2-1. b == 1인 경우 count += 1을 한다.
        2. count를 answer에 append한다.
    2. 결과를 반환한다.

    [Complexity]
    Time: O(N log N)
        - n + 1만큼 for-loop 순회
        - binary 변환 + binary_num 순회 -> O(log N) ?
    Space: O(N)
    """
    def countBits(self, n: int) -> List[int]:
        answer = []
        for num in range(n + 1):
            num_bin = bin(num)
            count = 0
            for b in num_bin:
                if b == '1':
                    count += 1
            answer.append(count)


        return answer

sol = Solution()
print(sol.countBits(100))
