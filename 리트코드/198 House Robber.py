"""
# 문제
198. House Robber
https://leetcode.com/problems/house-robber/

# 원인
풀이할 방법이 떠오르지 않음

# 내용
타뷸레이션을 이용한 풀이

파이썬 3.7부터 딕셔너리는 입력 순서가 유지 된다.
이전 버전은 입력 순서가 유지되지 않고, collections.OrderedDict 를 사용해서 유지할 수 있다.

# 참고자료
파이썬 알고리즘 인터뷰 책 p.642
"""
import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.popitem()[1]