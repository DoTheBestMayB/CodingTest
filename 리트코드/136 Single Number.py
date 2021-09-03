"""
# 문제
136. Single Number
https://leetcode.com/problems/single-number/

# 원인
시간복잡도 O(n) 공간복잡도 O(1)에 풀이할 방법이 떠오르지 않음

# 내용
십진수 변수에 nums 모든 값을 xor 하면 1개인 원소만 남게 된다.
두번 xor 하면 원래 값과 동일함을 이용

# 참고자료
파이썬 알고리즘 인터뷰 책 p.552
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
            print(result)

        return result
