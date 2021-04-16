"""
# 문제
238. LeetCode Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

# 내용
모든 배열의 원소를 곱하고, 원하는 원소의 값을 나누면 쉽게 해결할 수 있지만
나누기를 사용하지 않고 해결해야 하는 문제

왼쪽에서 부터 이전 index 원소를 곱해가고, 오른쪽에서 부터 이전 index 원소를 곱해서
나온 결과를 곱하면, 해당 index 를 제외하고 모두 곱한 결과값이 나옴

  A       B       C       D
  1       A      A*B    A*B*C
B*C*D    C*D      D       1
B*C*D   A*C*D   A*B*D   A*B*C

list 에서 list = list + [] 와 list += [] 는 새로운 리스트를 생성한다는 차이가 있지만
Int 변수에서 a = a + 3 과 a += 3 은 큰 차이가 없다
INPLACE_ADD 와 BINARY_ADD 의 차이가 있지만, 근소하게 INPLACE_ADD(+=) 가 더 빠름

dis 를 이용하면 파이썬 연산과정에서 차이점을 확인할 수 있다.
import dis
dis.dis(알고싶은 연산과정)

# 참고자료
파이썬 알고리즘 인터뷰 책
https://stackoverflow.com/questions/11925429/will-a-1-be-faster-than-a-a1-in-python
https://stackoverflow.com/questions/12905338/python-difference-between-x-x1-and-x-1
"""


def productExceptSelf(self, nums: list[int]) -> list[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


import time

st = time.time()
p = 1
for i in range(10**100):
    p = p * i
print(time.time() - st)

st = time.time()
p = 1
for i in range(10**100):
    p *= i
print(time.time() - st)