"""
# 문제
백준 1260번 DFS와 BFS
https://www.acmicpc.net/problem/1260

# 원인
BFS와 DFS 구현법을 몰랐음

# 참고자료
https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
"""


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        if graph.get(node) is not None:
            for neighbor in graph[node]:
                dfs(visited, graph, neighbor)


def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        if graph.get(node) is not None:
            for neighbor in graph[s]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


n, m, v = map(int, input().split())
node_dic = {}

for _ in range(m):
    x, y = map(int, input().split())
    if node_dic.get(x) is not None:
        node_dic[x].append(y)
    else:
        node_dic[x] = [y]

    if node_dic.get(y) is not None:
        node_dic[y].append(x)
    else:
        node_dic[y] = [x]

for dic_key in node_dic.keys():
    node_dic[dic_key].sort()


visited = set()
dfs(visited, node_dic, v)
print("")

visited = set()
queue = []
bfs(visited, node_dic, v)
