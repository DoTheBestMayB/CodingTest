"""
# 문제
21. LeetCode Merge Two Sorted Lists

# 내용
배열을 기존 배열에 이어 붙이고자 하는 경우 +=, extend 를 이용한다
두 개의 소요되는 시간 차이는 거의 없음
append 를 이용할 경우 배열 자체가 1개의 원소로 배열에 이어진다

# 참고자료
https://blog.finxter.com/python-list-concatenation-add-vs-inplace-add-vs-extend/#Method_3_Extend
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1, ptr2 = l1, l2
        output = None
        list_output = []

        l1_list = []
        while True:
            try:
                l1_list.append(ptr1.val)
                ptr1 = ptr1.next
            except AttributeError:
                break

        l2_list = []
        while True:
            try:
                l2_list.append(ptr2.val)
                ptr2 = ptr2.next
            except AttributeError:
                break

        ptr1, ptr2 = 0, 0
        while ptr1 < len(l1_list) and ptr2 < len(l2_list):
            if l1_list[ptr1] <= l2_list[ptr2]:
                list_output.append(l1_list[ptr1])
                ptr1 += 1
            else:
                list_output.append(l2_list[ptr2])
                ptr2 += 1

        if ptr1 < len(l1_list):
            list_output.extend(l1_list[ptr1:])
        elif ptr2 < len(l2_list):
            list_output.extend(l2_list[ptr2:])

        if len(list_output) == 0:
            output = None
        else:
            output = ListNode(list_output[0])
            ptr = output
            for idx in range(1, len(list_output)):
                ptr.next = ListNode(list_output[idx])
                ptr = ptr.next

        return output


l1 = ListNode(-9, ListNode(3))
l2 = ListNode(5, ListNode(7))

ans = Solution.mergeTwoLists(Solution, l1=l1, l2=l2)

while ans.next is not None:
    print(ans.val, end=' ')
    ans = ans.next
print(ans.val)