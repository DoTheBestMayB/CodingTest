"""
# 문제
LeetCode 200. Number of Islands
https://leetcode.com/problems/number-of-islands/submissions/

# 원인
DFS 를 코드로 구현하는 법을 몰랐음( 이웃한 네 곳의 노드를 방문하는 코드 )
DFS 탐색 시 Index Error 가 발생하는 경우(아래 코드)를 깔끔하게 해결하는 법이 안 떠올랐음
그러나 더 나은 방법을 찾아 볼 수 없었음
i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

# 참고자료
파이썬 알고리즘 인터뷰 책
"""
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count