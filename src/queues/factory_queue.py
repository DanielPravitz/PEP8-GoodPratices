from typing import Union

from queues.normal_queue import NormalQueue
from queues.priority_queue import PriorityQueue
from constants.constants import TYPE_QUEUE_NORMAL, TYPE_QUEUE_PRIORITY


class FactoryQueue:

    @staticmethod
    def get_queue(type_queue: str) -> Union[NormalQueue, PriorityQueue]:
        if type_queue == TYPE_QUEUE_NORMAL:
            return NormalQueue()

        elif type_queue == TYPE_QUEUE_PRIORITY:
            return PriorityQueue()

        else:
            raise NotImplementedError("Queue type doesn't exist!")
