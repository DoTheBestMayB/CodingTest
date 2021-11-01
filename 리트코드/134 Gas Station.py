"""
# 문제
134. Gas Station
https://leetcode.com/problems/gas-station/

# 원인
시작 지점을 바꿀때, 이전에 사용했던 결과를 재사용할 효율적인 방법이 떠오르지 않았음.

# 내용
canCompleteCircuit : 책의 코드 ( 452ms 48.98% )
canCompleteCircuitMy : 내가 작성한 코드 ( 4464ms 7.53% )

핵심 아이디어는 gas의 합이 cost의 합보다 크면 무조건 정답이 1개 있다는 것이다.
직접적인 반례를 찾지 못했지만, 생각하지 못한 반례가 있지 않을까란 생각에 station을 한바퀴 돌며 모두 확인해야 하는 코드로 작성했다.

하지만 그런 반례는 없으므로, sum(gas) < sum(cost) 이면, 무조건 정답이 1개 존재한다고 한다.
( 문제에서 정답이 존재하면 1개만 존재하는 경우만 케이스로 주어진다고 적혀 있음 )

# 참고자료
파이썬 알고리즘 인터뷰 책 p.599
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

    def canCompleteCircuitMy(self, gas: List[int], cost: List[int]) -> int:
        start_list = []
        sum = 0

        for idx in range(len(gas)):
            sum += gas[idx] - cost[idx]
            if gas[idx] != 0 and gas[idx] - cost[idx] >= 0:
                start_list.append(idx)

        if sum < 0:
            return -1

        for start_idx in start_list:
            remain = gas[start_idx] - cost[start_idx]
            if remain >= 0:
                idx = (start_idx + 1) % len(gas)
                is_right = True

                while idx != start_idx:
                    need = gas[idx] - cost[idx]
                    if remain + need >= 0:
                        remain += need
                        idx = (idx + 1) % len(gas)
                    else:
                        is_right = False
                        break

                if is_right:
                    return start_idx
        return -1