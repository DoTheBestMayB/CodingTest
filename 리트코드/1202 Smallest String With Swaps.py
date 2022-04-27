"""
# 문제
1202. Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/

# 내용
해결하는 방법은 떠올렸지만, 코드로 구현하는데 너무 오래 걸렸다.
이유는 기존에 작성한 코드에서 예외가 발생할 수 있는 디테일을 고려하지 않았기 때문이다.
"""

from typing import List

class Solution:
    def find_parent(self, parent, x) -> int:
        if parent[x] != x:
            parent[x] = self.find_parent(parent, parent[x])

        return parent[x]

    def union_parent(self, parent, a, b):
        a = self.find_parent(parent, a)
        b = self.find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if len(pairs) == 0:
            return s

        parent_of_s = [idx for idx in range(len(s))]

        for pair in pairs:
            if pair[0] == pair[1]:
                continue
            self.union_parent(parent_of_s, pair[0], pair[1])

        # Collect interchangeable characters into dictionary
        dic = {}
        for idx in range(len(s)):
            if parent_of_s[idx] in dic:
                dic[parent_of_s[idx]].append(idx)
            else:
                dic[parent_of_s[idx]] = [idx]

        # Handles a set of parents with different parent nodes.
        # ex) 0: [0, 1, 2, 3], 3: [4, 5, 6, 7]
        # parent of 3 is 3? No, it is 0
        # So, dic[3] is integrated to dic[0]
        for key in reversed(list(dic.keys())):
            if parent_of_s[key] != key:
                dic[parent_of_s[key]].extend(dic[key])
                dic.pop(key)

        # Relocate interchangeable characters in sorted order.
        char_list = ['' for _ in range(len(s))]
        for key in dic:
            list_of_index = dic[key]
            list_of_char = [s[x] for x in list_of_index]
            list_of_char.sort()
            list_of_index.sort()

            for index_of_s, index_of_char in zip(list_of_index, range(len(list_of_char))):
                char_list[index_of_s] = list_of_char[index_of_char]

        return ''.join(char_list)
