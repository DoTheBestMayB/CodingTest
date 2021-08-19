"""
# 문제
147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/

# 원인
Insert sort 를 효율적으로 하는 방법


# 내용
Insert Sort List 는 정답이 되는 List 의 뒷부분 부터 넣을 위치를 탐색하는데
이 문제는 이중 연결 리스트가 아니기 때문에 뒷부분 부터 탐색할 수 없어, 앞 부분부터 탐색한다.

이 때 매번 맨 앞 요소부터 탐색하지 않고, 이전에 탐색한 부분과 넣어야 할 값을 비교해서
'이전 탐색한 값 > 넣어야 할 값' 인 경우만 맨 앞 부분부터 탐색하는 방식으로 이전의 결과값을 이용한다.

insertionSortList : 계속 맨 처음부분 부터 탐색하는 방법 1760ms 43.36%
insertionSortListQuick : 이전에 탐색한 부분을 이용하는 방법 144ms 90.46%

# 참고자료
파이썬 알고리즘 인터뷰 책 p.500

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        head = head.next
        root.next = None

        while head is not None:
            cur = head
            head = head.next
            cur.next = None

            root_cur = root
            is_find = False
            while root_cur.next is not None:
                if cur.val <= root_cur.val:
                    root_cur.val, root_cur.next, cur.val, cur.next = cur.val, cur, root_cur.val, root_cur.next
                    is_find = True
                    break
                root_cur = root_cur.next
            if not is_find:
                if cur.val <= root_cur.val:
                    root_cur.val, root_cur.next, cur.val, cur.next = cur.val, cur, root_cur.val, root_cur.next
                else:
                    root_cur.next = cur

        return root

    def insertionSortListQuick(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = root_cur = head
        root_head = head.next
        root.next = None

        while root_head is not None:
            head_cur = root_head
            root_head = root_head.next
            head_cur.next = None

            if root_cur and head_cur.val < root_cur.val:  # 문제 되는 부분
                root_cur = root

            is_find = False
            while root_cur.next is not None:
                if head_cur.val <= root_cur.val:
                    root_cur.val, root_cur.next, head_cur.val, head_cur.next = head_cur.val, head_cur, root_cur.val, root_cur.next
                    is_find = True
                    break
                root_cur = root_cur.next

            if not is_find:
                if head_cur.val <= root_cur.val:
                    root_cur.val, root_cur.next, head_cur.val = head_cur.val, head_cur, root_cur.val
                else:
                    root_cur.next = head_cur
                root_cur = root_cur.next

        return root


if __name__ == '__main__':
    root = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    ans = Solution().insertionSortListQuick(root)