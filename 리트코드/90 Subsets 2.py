"""
# 문제
90. Subsets 2
https://leetcode.com/problems/subsets-ii/

# 내용
직접 작성한 코드
subsetsWithDupOrg : 처음에 생각해낸 아이디어. recursion 으로 얻은 결과에 현재 선택된 숫자를 각각 더하는 방식
subsetsWithDupSame : 중복된 숫자의 recursion 을 방지해서 시간을 줄임
list 를 append 하지 않고 + 함으로써 시간이 소요되는 문제를 해결하고 싶지만 아이디어가 떠오르지 않아서 리트코드에 질문 올림
https://leetcode.com/problems/subsets-ii/discuss/1383033/Python-skip-duplicate-element-Solution-20ms-but-can-be-reduced-help

다른 사람 코드
subsetsWithDup : 자신의 뒤 index 에 있는 요소만 접근하는 recursion 방식
ex) [1, 2, 3, 4, 5] 가 있을때
1은 2, 3, 4, 5 모두 접근 가능
2는 3, 4, 5 만 접근할 수 있음
3은 4, 5 만 접근할 수 있음

# 참고자료
https://leetcode.com/problems/subsets-ii/discuss/1381403/Python-solution-97.75-faster-just-used-tuple-instead-of-array
"""
from typing import List


class Solution:
    def subsetsWithDupSame(self, nums: List[int]) -> List[List[int]]:
        def get_sub(idx, sub_nums):
            if idx >= len_nums:
                return [[]]

            s_sets = []

            # check same element's length
            same_count = 0
            while idx + same_count < len_nums-1:
                if sub_nums[idx + same_count] == sub_nums[idx + same_count+1]:
                    same_count += 1
                else:
                    break

            if same_count == 0:
                sets = [sub_nums[idx]]
                idx += 1

                sub_sets = get_sub(idx, sub_nums)
                s_sets += sub_sets
                for sub_set in sub_sets:
                    s_sets.append(sub_set + sets)
            else:
                num = sub_nums[idx]
                idx += same_count + 1

                sub_sets = get_sub(idx, sub_nums)
                s_sets += sub_sets

                for i in range(same_count + 1):
                    element = [num for _ in range(i + 1)]
                    for sub_set in sub_sets:
                        s_sets.append(sub_set + element)

            return s_sets

        nums.sort()
        len_nums = len(nums)
        res = get_sub(0, nums)

        return res

    def subsetsWithDupOrg(self, nums: List[int]) -> List[List[int]]:
        def get_sub(sub_nums):
            if len(sub_nums) == 0:
                return [[]]

            s_sets = []

            num = sub_nums.pop()
            sub_sets = get_sub(sub_nums)

            s_sets += sub_sets

            for sub_set in sub_sets:
                if sub_set + [num] not in s_sets:
                    s_sets.append(sub_set + [num])

            return s_sets

        nums.sort()
        sets = []

        num = nums.pop()
        sub_sets = get_sub(nums)
        sets += sub_sets

        for sub_set in sub_sets:
            if sub_set + [num] not in sets:
                sets.append(sub_set + [num])

        return sets

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

            nums.sort()

            def recur(index, asf):

                ans.append(asf)

                if index >= len(nums):  # base case
                    return

                s = set()
                for i in range(index, len(nums)):
                    if nums[i] not in s:
                        s.add(nums[i])
                        recur(i + 1, asf + (nums[i],))

            # main====================================
            ans = []
            recur(0, tuple())
            return ans


if __name__ == '__main__':
    # nums = [4,4,4,1,4]
    # ans = Solution.subsetsWithDupOrg(Solution(), nums)
    nums = [1, 2, 2]
    ans2 = Solution.subsetsWithDupSame(Solution(), nums)
    # print(ans)
    print(ans2)