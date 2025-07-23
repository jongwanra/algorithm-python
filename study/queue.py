from collections import deque

queue = deque([1])
queue.append(2)

print(queue.popleft()) # 1
print(queue) # 2