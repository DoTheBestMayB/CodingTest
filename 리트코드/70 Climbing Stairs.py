"""
# 문제
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

# 원인
피보나치 수열과 같은 유형의 문제임을 알지 못함

# 내용
climbStairsBook: 책의 풀이( 피보나치 수열과 같은 문제로 보고 메모이제이션 이용)
climbStairs: 팩토리얼을 이용해서 내가 풀이한 방법

n의 최대 값이 45로 제한되어 있어 현재는 큰 차이가 없으나, n의 값이 매우 커지면 시간의 차이가 커진다.


# 참고자료
파이썬 알고리즘 인터뷰 책 p.639
"""
import collections
import time


class Solution:
    dp = collections.defaultdict(int)

    def climbStairsBook(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairsBook(n - 1) + self.climbStairsBook(n - 2)
        return self.dp[n]

    def climbStairs(self, n: int) -> int:
        def fact(num: int) -> int:
            res = 1
            for i in range(2, num + 1):
                res *= i

            return res

        ans = 0

        for two_num in range(0, n // 2 + 1):
            one_num = n - two_num * 2
            ans += fact(one_num + two_num) / fact(one_num) / fact(two_num)

        return int(ans)


if __name__ == '__main__':
    n = 500
    st = time.time()
    ans = Solution().climbStairs(n)
    print(time.time() - st)
