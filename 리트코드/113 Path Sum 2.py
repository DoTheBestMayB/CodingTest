"""
# 문제
113. Path Sum 2
https://leetcode.com/problems/path-sum-ii/

# 원인
1. root 부터 leaf 까지 쭉 이어지는 리스트 구해야함을 이해하지 못함
2. node.left 조건을 살필 때 return 하면 node.right 를 탐색할 수 없음을 고려하지 않음
> pathSumWrong

2. 음수 값을 가진 노드가 존재할 수 있다는 조건을 고려하지 않아, 중간에 sum 이 target_num 을 넘으면 DFS 탐색을 멈춰야 한다고 잘못 생각함
> pathSumCut

# 내용
문제의 조건으로부터 생각해봐야 할 것이 더 있는지 고민해보기
"""

import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, trace, sum):
            if sum == targetSum and node.left is None and node.right is None:
                ans.append(trace)
                return

            if node.left is not None:
                dfs(node.left, trace + [node.left.val], sum + node.left.val)

            if node.right is not None:
                dfs(node.right, trace+[node.right.val], sum+node.right.val)

        if root is None:
            return []

        ans = []
        dfs(root, [root.val], root.val)

        return ans

    def pathSumCut(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, trace, sum):
            if sum == targetSum and node.left is None and node.right is None:
                ans.append(trace)
                return

            if node.left is not None and sum + node.left.val <= targetSum:
                dfs(node.left, trace + [node.left.val], sum + node.left.val)

            if node.right is not None and sum + node.right.val <= targetSum:
                dfs(node.right, trace+[node.right.val], sum+node.right.val)

        if root is None:
            return []

        ans = []
        dfs(root, [root.val], root.val)

        return ans

    def pathSumWrong(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, trace, sum):
            if node is None:
                return False

            if node.left is not None:
                if sum + node.left.val == targetSum:
                    ans.append(trace + [node.left.val])
                    return True
                elif sum + node.left.val < targetSum:
                    dfs(node.left, trace + [node.left.val], sum + node.left.val)

            if node.right is not None:
                if sum + node.right.val == targetSum:
                    ans.append(trace + [node.right.val])
                    return True
                elif sum + node.right.val < targetSum:
                    dfs(node.right, trace + [node.right.val], sum + node.right.val)

        if root is None:
            return []
        elif root.val == targetSum:
            return [[root.val]]

        ans = []
        dfs(root, [root.val], root.val)

        return ans


def makeNode(root, ls):
    if len(ls) == 0:
        return 0

    ls.reverse()
    root.val = ls.pop()
    queue = collections.deque([root])

    while ls:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if ls:
                if ls[-1] is not None:
                    cur.left = TreeNode(val=ls.pop())
                    queue.append(cur.left)
                else:
                    ls.pop()

            if ls:
                if ls[-1] is not None:
                    cur.right = TreeNode(val=ls.pop())
                    queue.append(cur.right)
                else:
                    ls.pop()


def seekNode(root: TreeNode, max_depth: int):
    if not root:
        return
    queue = collections.deque([root])
    print(f'max depth is {max_depth}')
    now_depth = max_depth
    while queue:
        first_space = " " * int(((2 ** max_depth) * 2 - 1) / (len(queue)))
        for idx in range(len(queue)):
            if not(now_depth == 0 and idx == 0):
                print(first_space, end='')
            cur_root = queue.popleft()
            if now_depth == 0 or now_depth == max_depth:
                print(str(cur_root.val).ljust(2), end=' ')
            else:
                print(str(cur_root.val).rjust(2), end=' ')
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        print()
        now_depth -= 1


root = [1,-2,-3,1,3,-2,None,-1]
# root = [1,2]
tree_root = TreeNode()
makeNode(tree_root, root)
targetSum = -1
res = Solution.pathSum(Solution(), tree_root, targetSum)
print(res)