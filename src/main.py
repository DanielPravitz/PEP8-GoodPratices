# from normal_queue import NormalQueue
# from priority_queue import PriorityQueue
from queues.factory_queue import FactoryQueue
from statistics_classes.statistic_detailed import StatisticDetailed
from statistics_classes.statistic_summarized import StatisticSummarized


test = FactoryQueue.get_queue("priority")

for i in range(3):
    test.update_queue()
    print(test.call_client(i))

print(test.statistics(StatisticDetailed("05/09/2021", 120)))
