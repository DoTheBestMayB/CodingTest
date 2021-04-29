"""
# 문제
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

# 원인
ptr 은 3->4 에서 4->3으로 변경되었지만
head 의 2는 여전히 3을 가리키고 있음
즉, head 는 ptr 변경 직후 2 -> 1 -> 3 -> 4 에서 2 -> 1 -> 3 으로 됨

# 내용
node 를 swap 할 때, swap 하는 노드 뿐만 아니라 이 노드를 가리키는 노드도 변경해줘야 함
기존 node 가 A -> B 라면 A 를 가리키는 노드 X가 B를 가리키도록 변경해줘야 함

이 부분을 이해 하지 못해서 2시간 낭비함

swapPairs: prev 반영한 코드
swapPairsFail: prev 설정하지 않아 틀린 코드

# 참고자료
파이썬 알고리즘 인터뷰 책
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        head, head.next, head.next.next = head.next, head, head.next.next
        ptr = head.next.next
        prev = head.next

        while ptr and ptr.next:
            ptr, ptr.next, ptr.next.next = ptr.next, ptr, ptr.next.next
            prev.next = ptr

            ptr = ptr.next.next
            prev = prev.next.next

        return head

    def swapPairsFail(self, head: ListNode) -> ListNode:
        if not head:
            return head

        head, head.next, head.next.next = head.next, head, head.next.next
        ptr = head.next.next

        while ptr and ptr.next:
            ptr, ptr.next, ptr.next.next = ptr.next, ptr, ptr.next.next
            print(f'{ptr.val} {ptr.next.val}')
            ptr = ptr.next.next

        return head


def makeNode(input_arr: list) -> ListNode:
    if not input_arr:
        return None
    ln = ListNode(input_arr[0])
    res = ln
    for idx in range(1, len(input_arr)):
        ln.next = ListNode(input_arr[idx])
        ln = ln.next
    return res


l1 = makeNode([1])

ans = Solution.swapPairs(Solution(), head=l1)
while ans:
    print(ans.val, end=' ')
    ans = ans.next

