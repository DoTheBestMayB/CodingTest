"""
# 문제
316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/

# 원인
입력 문자열에서 중복을 확인하고, 앞 뒤 문자들과 비교하는 효율적인 방법을 생각해내지 못했음
2중 for 문을 이용해 전체 탐색하는 방법밖에 떠오르지 않았음

# 내용
재귀방식
1. 입력된 str 에 있는 알파벳을 오름차순으로 정렬해서 사전 순으로 낮은 알파벳부터 탐색
2. 입력된 str 중 선택된 알파벳(2개 이상 있다면 가장 앞에 있는 것)을 suffix 로 새로운 str 생성
3. 새로운 str 에 있는 알파벳이 입력된 str 에 있는 알파벳과 동일한지 확인
> 동일하다면 선택된 알파벳 앞을 모두 제거해도 괜찮음
> 사전 순으로 알파벳을 선택하므로, 선택된 알파벳보다 사전 순으로 앞선 알파벳은 입력으로 주어지지 않음
> str 알파벳이 동일 하다는 것은, suffix 앞에 문자들은 뒤에서 중복 등장하고, 선택된 알파벳보다 사전순으로 느리므로 삭제해도 됨

스택방식
collections.Counter : 아이템애 대한 개수를 계산해 딕셔너리로 리턴
키에는 아이템의 값, 값에는 해당 아이템의 개수가 들어감
파이썬 3.6 이하 : 딕셔너리는 입력 순서가 유지되지 않음
파이선 3.7 이후 : 내부적으로 인덱스를 이용해 입력 순서를 유지

ex) a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
>> Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

재귀 방식보다 스택 방식이 더 빠름

# 참고자료
파이썬 알고리즘 인터뷰 책
"""

import collections


class Solution:
    # 재귀를 이용한 분리
    def removeDuplicateLetters(self, s: str) -> str:
        # 사전 순서가 낮은 a부터 탐색
        for char in sorted(set(s)):
            # 방문한 char 앞을 짤라낸 string 생성
            suffix = s[s.index(char):]
            # 방문한 char 앞을 짤라내도 모든 알파벳이 포함되어 있는지 확인
            if set(s) == set(suffix):
                # 짤라낸 string 에서 방문한 char 를 모두 제거하고 재귀
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))

        return ''

    def removeDuplicateLettersStack(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            # 이미 처리된 문자 여부를 확인
            if char in seen:
                continue
            # 스택이 비어있지 않고 입력할 문자가 스택의 끝에 입력된 문자보다 사전순으로 앞이고
            # 스택의 끝에 입력된 문자가 뒤에서 등장할 예정이라면 스택에서 pop 한다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


input_str = "ebcabc"

print(Solution.removeDuplicateLettersStack(Solution(), input_str))