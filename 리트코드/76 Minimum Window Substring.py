"""
# 문제
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

# 원인
시간복잡도 O(n)에 풀이할 방법이 떠오르지 않음

# 내용
Key point: 투 포인터 left, right을 이용해 범위를 줄여가며 정답을 찾기

minWindowMy: 시간복잡도 O(n)에 풀리지 않는 생각해본 방법
minWindow: 브루트 포스로 풀이하는 책의 방법 1
minWindowPointer: 투 포인터를 이용해 풀이하는 책의 방법 2

# 참고자료
파이썬 알고리즘 인터뷰 책 p.575
"""
import collections
from typing import List


class Solution:
    def minWindowMy(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        deque = collections.deque()

        sub_t = list(t)
        short_len = -1
        left, right = -1, -1

        for idx, val in enumerate(s):
            try:
                sub_t.index(val)
                idx_t = sub_t.index(val)
                deque.append([idx, val])
                sub_t.pop(idx_t)
            except ValueError:
                if deque[0][1] == val:
                    deque.popleft()
                    deque.append([idx, val])
                elif deque[-1][1] == val:
                    deque.remove(val)
                    deque.append([idx, val])

            if len(sub_t) == 0 and (short_len == -1 or deque[-1][0] - deque[0][0] + 1 < short_len):
                left = deque[0][0]
                right = deque[-1][0]
                short_len = right - left + 1

        if short_len != -1:
            return s[left:right+1]
        else:
            return ''

    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_list: List):
            for t_elem in t_list:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ''

        window_size = len(t)

        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr

        return ''

    def minWindowPointer(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right

                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
