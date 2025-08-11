"""
[Problem]
https://leetcode.com/problems/decode-ways/

[Brainstorming]
숫자를 확인하면, decoding할 수 있는 자릿수는 한 자릿수, 두 자릿수로 제한적이다.
또한 1 ~ 26까지의 숫자의 경우에만 해당한다.

Dynamic Programming을 이용해서 해결하면 좋을 것 같다.

"12" = "1", "2" or "12"
"""


class AnotherSolution:
    """
    ref: https://www.algodale.com/problems/decode-ways/

    """
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(start:int):
            nonlocal s
            nonlocal memo
            # print(f"dfs({start}) - {s[start:]}")
            # 남아있는 숫자가 없다면 모든 숫자가 변환되었기 때문의 경우의 수를 한 가지 찾은 것과 동일하다.
            if start == len(s):
                return 1
            # 남아있는 숫자의 첫 번째 자리가 '0'인 경우 디코딩이 불가능하다.
            if s[start] == "0":
                return 0
            # 숫자가 2자리 이상 남아 있고 첫 두 자리가 변환 가능한 경우
            if start + 1 < len(s) and int(s[start:start+2]) < 27:
                if start + 1 not in memo:
                    memo[start + 1] = dfs(start + 1)
                if start + 2 not in memo:
                    memo[start + 2] = dfs(start + 2)

                return memo[start + 1] + memo[start + 2]

            if start + 1 not in memo:
                memo[start + 1] = dfs(start + 1)
            return memo[start + 1]
        return dfs(0)


sol = AnotherSolution()
print(sol.numDecodings("12") == 2)
print(sol.numDecodings("226") == 3)
print(sol.numDecodings("06") == 0)

