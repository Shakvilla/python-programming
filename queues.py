from collections import deque

queue = deque(["Abdul Shakur", 23, 45, 99, 89, "Books", True])

queue.append(False)
queue.popleft()
print(queue)
