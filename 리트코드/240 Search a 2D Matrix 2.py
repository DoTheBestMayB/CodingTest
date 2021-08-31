"""
# 문제
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

# 원인
첫 행, 첫 열부터 탐색하는 방법을 생각해봤는데, 백트래킹 하는 과정이 있어 코드가 복잡해져서 포기함

# 내용
첫 행의 맨 뒤 열부터 탐색하면 백트래킹 없이 해결할 수 있음
풀이 방법이 떠오르지 않으면 시작지점을 바꿔서 생각해보자

# 참고자료
파이썬 알고리즘 인터뷰 책 p.537
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False
