# I use double-ended-queue in this project

from collections import deque

# creating deque object
queue = deque()

# checking whether queue is empty or not -> True
print("queue is empty:")
print(len(queue) == 0)

# pushing the elements
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# again checking whether queue is empty or not -> False
print("queue is empty:")
print(len(queue) == 0)

# printing the queue
print("queue elements are:")
print(queue)

# removing the element -> 1
queue.popleft()

# printing the queue
print("queue elements are:")
print(queue)

# removing the element -> 1
print("queue elements are:")
queue.popleft()

# printing the queue
print(queue)

# removing all the elements
queue.popleft()
queue.popleft()
queue.popleft()


## checking the whether queue is empty or not for the last time -> True
print("queue is empty:")
print(len(queue) == 0)