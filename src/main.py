# from normal_queue import NormalQueue
# from priority_queue import PriorityQueue
from factory_queue import FactoryQueue


# test_queue = NormalQueue()

# for i in range(3):
#     test_queue.update_queue()

# print(test_queue.call_client(3))


# test_priority_queue = PriorityQueue()

# for i in range(3):
#     test_priority_queue.update_queue()
#     print(test_priority_queue.call_client(i))


# print(test_priority_queue.statistics("02-10-2021", 10, "detail"))

test = FactoryQueue.get_queue("normal")

for i in range(3):
   test.update_queue()
   print(test.call_client(i))