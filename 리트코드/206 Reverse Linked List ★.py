"""
# 문제
206. Reverse Linked List

# 원인
재귀적으로 구현하는 법을 생각해 내지 못했음

# 내용
재귀적으로 구현하는 방법
반복적으로 구현할 때 새로운 노드를 생성하지 않고 구현하는 방법
prev 라는 개념이 핵심

 지금 func -> 다음 func
next node -> 현재 node
현재 node -> prev node

현재 func 기준 : 현재 node 는 next node 의 next node
다음 func 기준 :  prev node 는 현재 node 의 next node

즉, 현재 node -> next node 에서 next node -> 현재 node 로 변경 됨

reverseList : 내가 반복적으로 구현한 코드( 새로운 Node 를 생성해서 해결함 )
reverseListIterate : 반복적으로 구현한 책의 답안( 코드가 더 간단하고, 기존 Node 의 연결만을 수정해서 구현함 )
reverseListRecurse : 재귀적으로 구현한 책의 답안

reverseListRecurse 이해하기 위한 흐름

1. reverse(1, None) next: 2 / 1->None
2. reverse(2, 1) next: 3 / 2->1
3. reverse(3, 2) next: 4 / 3->2
4. reverse(4, 3) next: 5 / 4->3
5. reverse(5, 4) next: None / 5->4
6. reverse(None, 5) return 5

return 5

# 참고자료
파이썬 알고리즘 인터뷰 책
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        if head is None:
            return ans

        while head.next is not None:
            ans, head = ListNode(head.val, ans), head.next
        if head is not None:
            ans = ListNode(head.val, ans)

        return ans

    def reverseListIterate(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def reverseListRecurse(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

ans = Solution.reverseListRecurse(Solution(), head=l1)

while ans.next is not None:
    print(ans.val, end=' ')
    ans = ans.next
print(ans.val)