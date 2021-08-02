"""
# 문제
1. Two Sum
https://leetcode.com/problems/two-sum/

# 내용
딕셔너리를 이용한 리스트 탐색 테크닉
리스트 탐색시 enumerate 까먹지 말기

# 참고자료
https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, value in enumerate(nums):
            remaining = target - value

            if remaining in seen:
                return [idx, seen[remaining]]
            else:
                seen[value] = idx


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution.twoSum(Solution(), nums, target))