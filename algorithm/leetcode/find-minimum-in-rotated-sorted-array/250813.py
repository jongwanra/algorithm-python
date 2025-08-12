"""
[Problem]
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

[Brainstorming]
최소값을 찾는 문제로 보인다.
앞에서 부터 값을 비교 하면서, 이전 요소가 현재 요소보다 큰 경우에 반환하면 된다. 없을 경우 가장 앞 요소가 최소값이다.
-> 이렇게 구현하면, 시간 복잡도는 O(nums.length)다.

O(log N)으로 풀 수있는 접근 방법을 모르기 때문에, 우선 O(nums.length)로 문제를 풀어 보자.

[Complexity]
Time: O(N)
Space: O(1)

"""
from typing import List
class Solution:
    def findMin(self, nums:List[int])->int:
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                return nums[index]
        return nums[0]


"""
ref: https://www.algodale.com/problems/find-minimum-in-rotated-sorted-array/
Binary Search를 활용해서 문제를 풀 수 있다. -> O(log N) 

[Complexity]
Time: O(log N)
Space: O(1)
"""
class AnotherSolution:
    def findMin(self, nums:List[int])->int:
        lt, rt = 1, len(nums) - 1

        while lt <= rt:
            m = (lt + rt) // 2
            # 바로 이전 값과 비교했을 때 대상이 더 작으면 최소값이다.
            if nums[m - 1] > nums[m]:
                return nums[m]
            if nums[0] < nums[m]:
                # nums[0]과 비교했을 때, 정렬되어 있다면 우리가 찾는 최소값은 0 ~ m 구간에는 없음을 의미한다.
                lt = m + 1
            else:
                rt = m - 1
        return nums[0]

sol = AnotherSolution()
print(sol.findMin([3, 4,5, 1, 2]) == 1)
print(sol.findMin([4,5,6,7,0,1,2]) == 0)
print(sol.findMin([11,13,15,17]) == 11)
print(sol.findMin([1]) == 1)
print(sol.findMin([2, 1]) == 1)
