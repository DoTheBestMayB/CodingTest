"""
# 문제
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

# 원인
max 값이 window를 벗어날 때, 다시 전체 탐색해서 시간 초과가 발생함

# 내용
maxSlidingWindowMy : 내가 작성한 코드, max 값과 max의 index를 기록하고 이것을 탐색한 값과 비교하는 방법을 사용함
maxSlidingWindow: 다른 사람이 작성한 코드

deque를 이용
탐색한 값과 deque에 있는 값을 비교해서, 탐색한 값보다 작으면 pop
> deque에는 항상 탐색한 값보다 큰 값들이 오름차순으로 정렬되어 있다.


# 참고자료
파이썬 알고리즘 인터뷰 책(p.571)
파이썬 알고리즘 인터뷰 깃허브 다른 사람의 풀이와 설명 ( https://github.com/onlybooks/algorithm-interview/issues/67 )
"""
import collections
from typing import List


class Solution:
    def maxSlidingWindowMy(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        max_num = -10 ** 4
        cnt = 0
        find_idx = k

        for idx, num in enumerate(nums[:k]):
            if num > max_num:
                max_num = num
                cnt = idx
        ans = [max_num]

        while find_idx < len(nums):
            if cnt > 0:
                if max_num < nums[find_idx]:
                    max_num = nums[find_idx]
                    cnt = k
            else:
                max_num = -10 ** 4
                for idx, num in enumerate(nums[find_idx + 1 - k:find_idx + 1]):
                    if num > max_num:
                        max_num = num
                        cnt = idx

            ans.append(max_num)
            cnt -= 1
            find_idx += 1

        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return results
