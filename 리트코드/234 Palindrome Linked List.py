"""
# 문제
234. LeetCode Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

# 원인
파이썬에서 Linked List 다루는 법을 몰랐음

# 내용
List : pop()은 O(1)이지만, pop(0)은 O(n)이다. 왜냐하면 모든 값을 한 칸씩 시프팅 해야 하기 때문이다.
파이썬 Deque : 이중 연결 리스트 구조로, pop(0)도 O(1)이다.
Deque 가 List 보다 2배 정도 빠름

역순으로 List 를 연결하는 방법( rev 는 역순으로 저장할 List, ptr 은 내용이 담긴 List )
rev, rev.next, ptr = ptr, rev, ptr.next

Runner 기법 : 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
> 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용함
2칸 씩 이동하는 Fast Runner 와 1칸 씩 이동하는 Slow Runner 를 만들어 계속 이동시키면
Fast Runner 가 끝에 도달했을때, Slow Runner 는 중간에 도달함( 입력값이 홀 수 일 경우 )
입력값이 짝수면 중간+1 칸에 위치함


공간복잡도에서 O(1)은 새로운 변수(주어진 변수 값을 가리키는 것 제외)를 생성하지 않고 주어진 변수만을 가지고 해결하는 것

# 참고자료
파이썬 알고리즘 인터뷰 책
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: list = []
        # Deque 는 위 문장 대신
        # q = collections.deque()

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            # Deque 는 아래 문장 사용
            # q.popleft() != q.pop()
            if q.pop(0) != q.pop():
                return False

        return True

    def isPalindromeRunner(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev