"""
# 문제
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

# 원인
코드를 줄여주는 파이썬 기본 기능을 새로 알게됨

# 내용
기본 dictionary 사용
> numJewelsInStones Function

collections.defaultdict(parameter) : 존재하지 않는 키에 대해 디폴트(parameter로 전달해주는 것)을 리턴해줌
> useDict Function

collections.Counter(S) : parameter로 입력된 S에 포함된 문자의 개수를 계산함. 존재하지 않는 키는 0 출력해줌
> useCounter Function

# 출처
https://www.geeksforgeeks.org/defaultdict-in-python/
파이썬 알고리즘 인터뷰 책
"""
import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict_input = {}
        ans = 0

        for stone in stones:
            if stone in dict_input:
                dict_input[stone] += 1
            else:
                dict_input[stone] = 1

        for jewel in jewels:
            if jewel in dict_input:
                ans += dict_input[jewel]

        return ans

    def useDict(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1

        for char in J:
            count += freqs[char]

        return count

    def useCounter(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)
        count = 0

        for char in J:
            count += freqs[char]

        return count