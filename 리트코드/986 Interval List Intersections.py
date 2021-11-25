"""
# 문제
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections

# 원인
1. 포인터를 이용해 간단하게 풀이하지 못함
2. 시간이 많이 소요되는 원인을 찾지 못함

# 내용
1. 모든 케이스를 분류하고, if 문으로 표현하려다보니 코드가 복잡해지고 빠진 케이스가 있는지 확인하기 어려움
> left, right pointer 를 이용해서 해결

2. left, right를 이용해서 시간을 단축시켰지만, 시간이 많이 소요되는 원인을 찾지 못했음
> 61번, 65번 라인의 불필요한 값 변경이 원인이였음
재사용하는 포인터의 left 범위를 줄여줘야 한다고 생각해서 입력한 코드인데
left, right 의 값을 비교하므로, 범위를 줄여줄 필요가 없다.
> submission detail 에서 시간이 빠른 제출자의 코드와 내 코드 비교를 통해 값 대입이 필요 없음을 깨달음
"""
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len_first, len_second = len(firstList), len(secondList)
        if len_first == 0 or len_second == 0:
            return []
        ans = []
        pointer_first, pointer_second = 0, 0

        while pointer_first < len_first and pointer_second < len_second:
            first = firstList[pointer_first]
            second = secondList[pointer_second]

            # 겹치는 범위가 없는 경우
            if first[1] < second[0]:
                pointer_first += 1
                continue
            elif second[1] < first[0]:
                pointer_second += 1
                continue

            # 끝 부분만 겹치는 경우
            if first[1] == second[0]:
                ans.append([first[1], first[1]])
                pointer_first += 1
                continue
            elif second[1] == first[0]:
                ans.append([second[1], second[1]])
                pointer_second += 1
                continue

            # Left
            if first[0] <= second[0]:
                left = second[0]
            else:
                left = first[0]

            # right
            if first[1] <= second[1]:
                right = first[1]
                pointer_first += 1
                # secondList[pointer_second][0] = right  # 런타임에 많은 부분을 차지한 부분. 굳이 없어도 됨
            else:
                right = second[1]
                pointer_second += 1
                # firstList[pointer_first][0] = right  # 런타임에 많은 부분을 차지한 부분. 굳이 없어도 됨

            ans.append([left, right])

        return ans
