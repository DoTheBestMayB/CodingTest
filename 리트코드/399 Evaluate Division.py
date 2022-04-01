"""
# 문제
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

# 원인
구현하기 복잡하면 천천히 꼼꼼하게 작성하기

# 내용
계속 틀리면서 테스트 케이스 보면서 뭐가 틀렸는지 디버깅으로 고쳤다.
만약 디버깅을 할 수 없는 시험 환경이라면 어떻게 구현할지는 알지만 제대로 구현하지 못해 틀렸을 것이다.
"""

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(graph, v, visited, find_value):
            if find_value in graph[v]:
                if [v, find_value] not in equations:
                    return 1 / values[equations.index([find_value, v])]
                return values[equations.index([v, find_value])]
            visited[v] = True

            for i in graph[v]:
                if visited[i]:
                    continue
                res = dfs(graph, i, visited, find_value)
                if res != -1.0:
                    if [v, i] not in equations:
                        return res / values[equations.index([i, v])]
                    return res * values[equations.index([v, i])]

            return -1.0

        dict = {}
        equation_alphabet = []

        for equation in equations:
            if equation[0] not in dict:
                dict[equation[0]] = [equation[1]]
            else:
                dict[equation[0]].append(equation[1])

            equation_alphabet.append(equation[0])
            if equation[0] != equation[1]:
                if equation[1] not in dict:
                    dict[equation[1]] = [equation[0]]
                else:
                    dict[equation[1]].append(equation[0])
                equation_alphabet.append(equation[1])

        answer = []
        for query in queries:
            if query[0] not in equation_alphabet or query[1] not in equation_alphabet:
                answer.append(-1.0)
                continue

            visited = {}
            for alphabet in equation_alphabet:
                visited[alphabet] = False
            res = dfs(dict, query[0], visited, query[1])
            answer.append(res)
        return answer


if __name__ == '__main__':
    equations = [["a", "aa"]]
    values = [9.0]
    queries = [["aa","a"],["aa","aa"]]
    output = Solution().calcEquation(equations, values, queries)
    print(output)