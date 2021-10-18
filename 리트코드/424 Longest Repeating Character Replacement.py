"""
# 문제
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

# 원인
문자를 변경할 구간을 어떻게 정해야 할지 생각해내지 못함

# 내용
characterReplacementMy: 내가 생각해낸 방법 ( 시간 초과 )
characterReplacementM: 책의 코드

# 참고자료
파이썬 알고리즘 인터뷰 책 p.552
"""
import collections


class Solution:
    def characterReplacementMy(self, s: str, k: int) -> int:
        left = 0
        left_k = k
        ans = 0
        count = 1
        right = 1
        visited_char = collections.defaultdict(int)
        is_first = True
        ch = s[left]

        while len(s) - left > ans and right < len(s):
            if ch == s[right]:
                count += 1
                right += 1
            else:
                if left_k > 0:
                    if is_first:
                        visited_char[s[right]] += 1
                    left_k -= 1
                    count += 1
                    right += 1
                else:
                    if count > ans:
                        ans = count

                    if is_first and visited_char and k > 0:
                        is_first = False
                        count = 1
                        left_k = k - 1
                        right = left + 1

                        cnt = 0
                        for key in visited_char:
                            if visited_char[key] > cnt:
                                cnt = visited_char[key]
                                ch = key

                        continue

                    while s[left] == ch:
                        left += 1

                    right = left + 1
                    count = 1
                    left_k = k
                    ch = s[left]
                    visited_char = collections.defaultdict(int)
        if count > ans:
            return count
        else:
            return ans

    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left