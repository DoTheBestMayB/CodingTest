"""
# 문제
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# 원인
1. 경우의 수를 꼼꼼히 나누지 못해서, 나누는 조건을 틀림
2. 문제 해결에 도움이 되는 특징을 찾지 못함

# 내용
경우의 수를 나눌때는 머리속으로 만 생각하지 말고 될 수 있는 경우의 수를 직접 노트에 적어보기

항상 맨 앞 원소가 맨 뒤 원소보다 크거나 같다
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) < 4:
            if target in nums:
                return True
            else:
                return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[0] < nums[mid]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[0] > nums[mid]:
                right = mid - 1
            elif nums[0] == nums[mid]:
                if target < nums[0]:
                    for idx in range(1, mid):
                        if nums[idx] < nums[0]:
                            return self.search(nums[idx:mid], target)
                    for idx in range(mid, len(nums)):
                        if nums[idx] < nums[0]:
                            return self.search(nums[idx:], target)
                    return False
                elif target > nums[0]:
                    for idx in range(1, mid):
                        if nums[idx] > nums[0]:
                            return self.search(nums[idx:mid], target)
                    for idx in range(mid, len(nums)):
                        if nums[idx] > nums[0]:
                            return self.search(nums[idx:], target)
                    return False
        return False


if __name__ == '__main__':
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    ans = Solution().search(nums, target)
    print(ans)
