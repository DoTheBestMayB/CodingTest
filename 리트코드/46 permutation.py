"""
# 문제
46. Permutations
https://leetcode.com/problems/permutations/

# 원인
처음에 리스트에 숫자를 담아서 처리하는 방식으로 코드를 작성했는데
리스트가 아닌 string 으로 만들어서 처리하면 더 빠르지 않을까란 생각에서 코드를 작성해봤다

하지만 string 으로 변환된 음수를 처리하기가 복잡하고
9보다 큰 혹은 -9보다 작은 숫자가 입력으로 주어지면 더 복잡해진다.

# 내용
permute : 리스트로 해결한 코드
permuteString : string 으로 변환해서 해결한 코드( -9보다 작거나, 9보다 큰 숫자가 입력으로 주어지면 틀림 )

permute 40ms, permuteString 44ms로 실행시간에 큰 차이 없음

문제에서 양수가 아닌 음수도 입력으로 주어지기 때문에 음수를 처리하는 부가적인 코드로 계산 과정이 늘어남
또한 처음에 리스트를 string 으로과 마지막에 리스트를 string 으로 변환하는 과정이 필요함
10이상, -10 이하인 숫자가 주어졌을때 이것을 string 에서 파악하기 어려움( 10 인지 혹은 1, 0 인지 )

"""
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(nums: list[int]):
            res = []
            for num in nums:
                if len(nums) > 1:
                    t_nums = nums + []
                    t_nums.remove(num)
                    sub_res = dfs(t_nums)

                    for sub in sub_res:
                        res.append([num] + sub)
                else:
                    res.append([num])

            return res

        return dfs(nums)

    def permuteString(self, nums: list[int]) -> list[list[int]]:
        def dfs(nums: str):
            res = []
            is_minus = False
            for num in nums:
                if num == "-":
                    is_minus = True
                    continue
                if (len(nums) > 1 and '-' not in nums) or (len(nums) > 2 and '-' in nums):
                    t_nums = nums.replace(num, '', 1)
                    if is_minus:
                        t_nums = t_nums.replace('-', '', 1)
                    sub_res = dfs(t_nums)

                    for sub in sub_res:
                        if is_minus:
                            res.append("-" + num + sub)
                        else:
                            res.append(num + sub)
                else:
                    if is_minus:
                        res.append("-"+num)
                    else:
                        res.append(num)
                is_minus = False
            return res

        ch = "".join([str(elem) for elem in nums])
        t_res = dfs(ch)
        # print(f't_res : {t_res}')
        res = []

        is_minus = False
        for arr in t_res:
            t_arr = []
            for ch in arr:
                if ch == '-':
                    is_minus = True
                    continue
                if is_minus:
                    t_arr.append(int('-'+ch))
                else:
                    t_arr.append(int(ch))
                is_minus = False
            res.append(t_arr)
        return res

