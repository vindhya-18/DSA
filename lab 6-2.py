from collections import deque

queue = deque([10, 20, 30])

print("Before dequeue:", queue)

# Remove front element
deleted = queue.popleft()

print("Deleted element:", deleted)
print("After dequeue:", queue)
