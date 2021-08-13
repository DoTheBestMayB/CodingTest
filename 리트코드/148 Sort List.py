"""
# 문제
148. Sort List
https://leetcode.com/problems/sort-list/

# 원인
연결 리스트에 merge sort 사용하는 법을 떠올리지 못함

# 내용
연결 리스트에 merge sort 사용하는 방법
1. 런너 기법(p.207)을 사용해서 입력 리스트의 중앙 원소를 구한다 [ Divide ]
slow가 중앙 원소에 해당함
half, slow, fast
while fast and fast.next:
    half, slow, fast = slow, slow.next, fast.next.next
half.next = None # 중앙 원소를 기준으로 연결 관계를 끊음

2. 좌,우 두 개의 LinkedList에 대해 재귀 호출
l1 = self.sortList(head)
l2 = self.sortList(slow)

3. l1, l2를 다시 합친다 [ Conquer ]
self.mergeTwoLists(l1, l2)
l1과 l2의 값을 비교해서 작은 순서대로 이어 붙임

def mergeTwoLists(self, l1, l2):
    if l1 and l2:
        # 작은 값을 l1으로
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2


# 참고자료
파이썬 알고리즘 인터뷰 책(p.489)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

