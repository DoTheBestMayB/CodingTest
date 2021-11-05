"""
# 문제
241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

# 원인
분할정복 풀이법을 코드로 구현하지 못함

# 참고자료
파이썬 알고리즘 인터뷰 책 p.618
"""
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []

            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])

                results.extend(compute(left, right, value))

        return results