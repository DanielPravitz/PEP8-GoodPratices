from typing import Union

from normal_queue import NormalQueue
from priority_queue import PriorityQueue
from constants import TYPE_QUEUE_NORMAL, TYPE_QUEUE_PRIORITY

class FactoryQueue:

    @staticmethod
    def get_queue(type_queue: str) -> Union[NormalQueue, PriorityQueue] :
        if type_queue == TYPE_QUEUE_NORMAL:
            return NormalQueue()

        elif type_queue == TYPE_QUEUE_PRIORITY:
            return PriorityQueue()

        else:
            raise NotImplementedError("Queue type doesn't exist!")
