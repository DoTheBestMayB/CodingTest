"""
# 문제
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/

# 원인
사전순으로 작은 것부터 방문하면 문제가 해결되지 않는 반례가 존재할 것 같아
이것을 확인하고 예외 처리하는 코드를 추가했는데

사전순으로 방문하면서 예외가 발생하지 않도록 하는 방법이 있었음

# 내용
findItinerary: 내가 구현한 코드
findItineraryGreedy: Greedy 로 풀이하면서 예외가 발생하지 않는 책의 코드

1. 사전순으로 앞에 있는 방문지를 먼저 방문한다.
2. 그 곳에서 또 방문지가 있으면 1번을 반복한다.
3. 더 이상 방문지가 없으면 루트에 입력한다.
4. 루트를 거꾸로 하면 정답

사전순으로 방문해서 쭉 이어지면 > 정답
사전순으로 방문했는데 중간에 막히면 > 루트를 거꾸로 만들것 이기 때문에 마지막에 방문하게 되므로 괜찮음
>> 이 부분을 이해하는데 오래 걸림. 반례가 있지 않을까 계속 생각해봤는데 못찾았음

# 참고 자료
파이썬 알고리즘 인터뷰 책
"""


import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def dfs(start, depth):
            # print(start)
            result.append(start)
            # print(start)
            if depth == len(tickets):
                return True

            if start not in dic:
                result.pop()
                return False

            for j in range(0, len(dic[start])):
                if dic[start][j][1] == 0:
                    dic[start][j][1] = 1
                else:
                    continue
                if dfs(dic[start][j][0], depth+1):
                    return True
                else:
                    dic[start][j][1] = 0

            result.pop()
            return False

        # tickets 를 dict 로 변환하기
        dic = {}

        for ticket in tickets:
            if ticket[0] in dic:
                dic[ticket[0]].append([ticket[1], 0])
            else:
                dic[ticket[0]] = [[ticket[1], 0]]

        # value 정렬하기
        for i in dic.keys():
            dic[i] = sorted(dic[i])
        first_key = 'JFK'
        result = [first_key]

        for j in range(0, len(dic[first_key])):
            dic[first_key][j][1] = 1

            if dfs(dic[first_key][j][0], 1):
                return result
            else:
                dic[first_key][j][1] = 0
        result.pop()

        return result

    def findItineraryGreedy(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        print(graph)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')

        return route[::-1]

tickets = [['JFK', 'ABC'], ['JFK', 'CDF'], ['ABC', 'JFK'], ['ABC', 'BCD'], ['BCD', 'ABC']]
ans = Solution.findItinerary(Solution(), tickets)

print(ans)

