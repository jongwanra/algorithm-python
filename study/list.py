
# 1차원 리스트 구현
visited = [False] * 5
print(visited)

visited[0] = True

print(visited)

# 2차원 리스트 구현
graph = []
row = 5
col = 3
graph = [[False] * col for _ in range(row)]

graph[0][0] = True
print(graph)