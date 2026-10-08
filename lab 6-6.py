from collections import deque

queue = deque()

# 1. ENQUEUE
queue.append(10)
queue.append(20)
queue.append(30)

print("After enqueue:", list(queue))

# 2. DEQUEUE
deleted = queue.popleft()
print("Deleted:", deleted)

# 3. PEEK
print("Front element:", queue[0])

# 4. IS EMPTY
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")

# 5. DISPLAY
print("Queue:", list(queue))
