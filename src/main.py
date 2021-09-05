from normal_queue import NormalQueue
from priority_queue import PriorityQueue

# test_queue = NormalQueue()

# for i in range(3):
#     test_queue.update_queue()

# print(test_queue.call_client(3))


test_priority_queue = PriorityQueue()

for i in range(3):
    test_priority_queue.update_queue()
    print(test_priority_queue.call_client(i))


print(test_priority_queue.statistics("02-10-2021", 10, "detail"))
