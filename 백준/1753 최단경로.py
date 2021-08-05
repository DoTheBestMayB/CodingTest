"""
# 문제
백준 1753번 최단경로
https://www.acmicpc.net/problem/1753

# 원인
입력이 많을때 input()을 사용하면 시간이 오래 걸린다
> prompt message 출력 처리 과정이 있음
> 입력받은 값의 개행 문자를 삭제시키는 과정이 있음

# 내용
prompt message 예시
input("prompt message")
> prompt message

sys.stdin.readline()을 이용하면 많은 입력이 주어져도 빠르게 처리 가능
> 파라미터로 최대 입력 갯수를 설정함
> 개행 문자를 포함한 값을 리턴함


# 참고자료
이것이 취업을 위한 코딩 테스트다 책
https://buyandpray.tistory.com/7
https://www.geeksforgeeks.org/taking-input-in-python/
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

q = []
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

