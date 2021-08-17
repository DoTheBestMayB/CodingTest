"""
# 문제
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

# 내용
merge: merge sort로 intervals를 정렬함(직접 작성한 코드) 144ms 5.27%
merge_book: 파이썬 내장함수 sort로 intervals를 정렬함(책에 있는 코드) 80ms 90.98%

# 참고자료
파이썬 알고리즘 인터뷰 책 p.497
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort_list(intervals):
            if len(intervals) < 2:
                return intervals

            slow, fast = 0, 0
            while fast < len(intervals) - 1:
                slow, fast = slow + 1, fast + 2

            l1 = sort_list(intervals[0:slow])
            l2 = sort_list(intervals[slow:])

            return merge_two_lists(l1, l2)

        def merge_two_lists(l1, l2):
            l1_cur = l1[0]
            l2_cur = l2[0]

            # print(l1)
            if l1_cur[0] > l2_cur[0]:
                l1_cur[0], l2_cur[0] = l2_cur[0], l1_cur[0]
                l1_cur[1], l2_cur[1] = l2_cur[1], l1_cur[1]

                if len(l1) > 1:
                    l1[1:] = merge_two_lists(l1[1:], l2)
                else:
                    if len(l2) > 1:
                        l2 = sort_list(l2)
                    l1 += l2
            else:
                if l1_cur[0] == l2_cur[0] and l1_cur[1] > l2_cur[1]:
                    l1_cur[1], l2_cur[1] = l2_cur[1], l1_cur[1]
                if len(l1) > 1:
                    l1[1:] = merge_two_lists(l1[1:], l2)
                else:
                    if len(l2) > 1:
                        l2 = sort_list(l2)
                    l1 += l2

            return l1

        if len(intervals) <= 1:
            return intervals

        # interval를 오름차순 정렬
        intervals = sort_list(intervals)
        print(intervals)

        # intervals 를 탐색하며 interval 정리하기
        ans = []
        interval_start = -1
        interval_end = -1
        for idx in range(0, len(intervals)-1):
            if interval_start == -1:
                if intervals[idx][1] >= intervals[idx+1][0]:
                    interval_start = intervals[idx][0]

                    if intervals[idx][1] >= intervals[idx+1][1]:
                        interval_end = intervals[idx][1]
                    else:
                        interval_end = intervals[idx+1][1]
                else:
                    ans.append(intervals[idx])
            else:
                if interval_end < intervals[idx+1][0]:
                    ans.append([interval_start, interval_end])
                    interval_start = -1
                    interval_end = -1
                elif interval_end < intervals[idx+1][1]:
                    interval_end = intervals[idx+1][1]

        if interval_start != -1:
            ans.append([interval_start, interval_end])
        else:
            ans.append(intervals[-1])

        return ans

    def merge_book(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged


if __name__ == '__main__':
    intervals = [[0,0],[1,2],[5,5],[2,4],[3,3],[5,6],[5,6],[4,6],[0,0],[1,2],[0,2],[4,5]]
    # intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    ans = Solution().merge(intervals)
    print(ans)