"""
# 문제
78. Subsets
https://leetcode.com/problems/subsets/

# 내용
dfs 로 탐색한 경로를 저장할 때, 더 효율적인 방법
append 를 최대한 적게 사용해야 함

subsets : 내가 작성한 방법
subsetsMore : 더 효율적인 방법

# 참고자료
파이썬 알고리즘 인터뷰 책
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(idx_start: int):
            r_set = []
            for idx in range(idx_start, idx_end):
                t_set = [nums[idx]]

                r_set += t_set
                sub_res = dfs(idx + 1)
                for s in sub_res:
                    r_set.append(t_set + s)

            return r_set

        idx_end = len(nums)
        res = dfs(0)
        res.append([])
        return res

    def subsetsMore(self, nums: list[int]) -> list[list[int]]:
        def dfs(idx, path):
            result.append(path)

            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])

        result = []
        dfs(0, [])
        return result

nums = [1,2,3]
ans = Solution.subsets(Solution(), nums)

print(ans)

