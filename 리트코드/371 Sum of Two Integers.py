"""
# 문제
371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/

# 원인
전가산기 코드를 구현하지 못함

# 내용
getSum: 전가산기 개념을 그대로 구현한 코드(책에 적힌 코드)
getSumShort: 필요한 전가산기 개념만 구현한 코드(책에 적힌 코드)

# 참고자료
파이썬 알고리즘 인터뷰 책 p.555

"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # 전가산기 구현
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))
        if carry == 1:
            result.append('1')

        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        # 음수 처리
        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result

    def getSumShort(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        # 합, 자릿수 처리
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 음수 처리
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a