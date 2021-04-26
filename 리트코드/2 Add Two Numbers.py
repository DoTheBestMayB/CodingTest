"""
# 문제
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

# 원인
while 조건문을 어떻게 설정할지 고민하느라 오래 걸림
1. node.next 가 None 인 경우로 할 것 인지, node 가 None 인 경우로 할 것 인지
2. l1 만 None 인 경우, l2 만 None 인 경우, l1 과 l2 모두 None 인 경우를 어떻게 처리 할 것 인지

# 내용
addTwoNumbers : 내 답안
addTwoNumbers2 : 책 답안

1번
ListNode 문제에서 node.next 를 미리 만들어두면 마지막에 불필요한 node 가 붙음 ( 결과가 XXX0 처럼 됨 )
.
내가 작성한 답안의 경우, 방문 node 의 초깃값을 None 으로 두고 while 문 안에서 첫 node 방문인지 확인하는 조건을 넣었음
> 처음을 제외하면 불필요한 조건 확인이 반복됨

책에서는 node 의 초깃값을 ListNode(0) 로 두고 생성되는 node 를 next 로 계속 이어 붙임
return 할 때는 처음 node 를 제외하고 return 함으로써 간단하게 해결함 ( root.next )

2번
나는 l1 과 l2 의 value 가 모두 존재하는 경우와, l1 혹은 l2 만 존재하는 경우를 나눠서 풀이함
이 때문에 유사한 코드가 반복되어 코드가 길어짐
> l1 and l2

책에서는 따로 나누지 않고, while 문 내부에서 l1 이 존재하는지 l2 가 존재하는지 확인 함
> l1 or l2
> if l1:, if l2:

문제에서 요구하는 두 배열 원소의 덧셈은 l1 의 원소 + l2 의 원소이다.
따라서 l1 이 존재하는지 확인해서 있다면 더하고, l2도 똑같이 하면 된다.
반면 나는 l1 과 l2 를 함께 더하려고만 생각해서, 적절한 조건을 짜지 못했다.

조건을 짤 때, 최대한 합쳐서 간단하게 나타내려 하기 보다는 작은 부분으로 나눠 풀어가는게 더 좋은 접근이다.

1 부터 n 까지 더하는 문제에서 for 문을 통해 하나 하나 더하는 방법 대신 수학 공식 n(n+1)/2 로 O(1)로 나타내는 방법을 본 뒤로
최대한 합치려는 생각에 억매인 것 같다.

# 참고자료
파이썬 알고리즘 인터뷰 책
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr_l1, ptr_l2 = l1, l2
        ans = None
        ptr_ans = ans

        carry_num = 0
        while ptr_l1 and ptr_l2:
            sum_num = ptr_l1.val + ptr_l2.val + carry_num
            carry_num = sum_num // 10

            if ptr_ans:
                ptr_ans.next = ListNode(sum_num % 10)
                ptr_ans = ptr_ans.next
            else:
                ptr_ans = ListNode(sum_num % 10)
                ans = ptr_ans

            ptr_l1 = ptr_l1.next
            ptr_l2 = ptr_l2.next

        if ptr_l1:
            ptr_more = ptr_l1
        else:
            ptr_more = ptr_l2

        while ptr_more:
            sum_num = ptr_more.val + carry_num
            carry_num = sum_num // 10

            ptr_ans.next = ListNode(sum_num % 10)
            ptr_ans = ptr_ans.next

            ptr_more = ptr_more.next

        if carry_num != 0:
            ptr_ans.next = ListNode(carry_num)

        return ans

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


def makeNode(input_arr: list) -> ListNode:
    ln = ListNode(input_arr[0])
    res = ln
    for idx in range(1, len(input_arr)):
        ln.next = ListNode(input_arr[idx])
        ln = ln.next
    return res


l1 = makeNode([9,9,9,9,9,9,9])
l2 = makeNode([9,9,9,9])

ans = Solution.addTwoNumbers(Solution(), l1, l2)

while ans.next is not None:
    print(ans.val, end=' ')
    ans = ans.next
print(ans.val)