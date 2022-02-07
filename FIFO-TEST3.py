from queue import Queue

## creating Queue object
queue_object = Queue()

## checking whether queue is empty or not -> True
print("queue is empty:")
print(queue_object.empty())

## adding the elements
queue_object.put(1)
queue_object.put(2)
queue_object.put(3)
queue_object.put(4)
queue_object.put(5)

## again checking whether queue is empty or not -> False
print("queue is empty:")
print(queue_object.empty())

## removing all the elements
print(queue_object.get())
print(queue_object.get())
print(queue_object.get())

## checking the queue size
#print("Size", queue_object.qsize())

print(queue_object.get())
print(queue_object.get())

## checking the whether queue_object is empty or not for the last time -> True
print("queue is empty:")
print(queue_object.empty())
