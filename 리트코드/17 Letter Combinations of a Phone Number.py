"""
# 문제
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# 원인
숫자와 문자가 특정한 규칙에 따라 쌍을 이룰때
아스키 코드값을 이용해(chr(), ord()) 변환하는 방법만을 생각했는데
딕셔너리를 이용하는 방법도 있음을 알게되었음

# 내용
두 방식의 실행 시간 차이는 거의 없다
아스키 코드 값을 이용하려면 변환하는 규칙을 찾아야 하고, 예외를 생각하느라 시간이 오래 걸린다
앞으로는 dictionary 를 이용하는 방법을 우선적으로 생각해야겠다

Solution: 아스키 코드 값을 이용해 내가 구현한 코드
Solution2: dictionary 를 이용해 숫자-문자 쌍을 만들어 해결한 코드

# 참고자료
파이썬 알고리즘 인터뷰 책
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(digits: str):
            if digits == "":
                return []
            res = []
            correction_num = 0
            range_len = 3
            digit = int(digits[0])
            if digit >= 8:
                correction_num = 1
            if digit in [7, 9]:
                range_len = 4

            for idx in range(0, range_len):
                letter = chr((digit - 2) * 3 + 97 + correction_num + idx)

                if len(digits) >= 2:
                    sub_res = dfs(digits[1:])
                    for sub in sub_res:
                        res.append(letter + sub)
                else:
                    res.append(letter)

            return res

        return dfs(digits)


class Solution2:
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in dic[digits[index]]:
                dfs(index + 1, path + i)

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result
