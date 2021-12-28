"""
# 문제
231. Power of Two
https://leetcode.com/problems/power-of-two/

# 원인
비트 연산을 통해 2의 배수는 1000...(2) 로 나타내진다는 것을 생각해내지 못함
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        sub_str = str(bin(n))[3:]
        if sub_str == '' or int(sub_str) == 0:
            return True
        else:
            return False