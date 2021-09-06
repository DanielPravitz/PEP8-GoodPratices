from typing import Union

from queues.base_queue import BaseQueue
from constants.constants import PRIORITY_CODE
from statistics_classes.statistic_detailed import StatisticDetailed
from statistics_classes.statistic_summarized import StatisticSummarized

statistic_type = Union[StatisticDetailed, StatisticSummarized]


class PriorityQueue(BaseQueue):

    def password_generator(self) -> None:
        self.password = f"${PRIORITY_CODE}{self.code}"

    def call_client(self, cashier: int) -> str:
        actual_client: str = self.queue.pop(0)
        self.clients.append(actual_client)

        return(f"Client number {actual_client} , go to cashier {cashier}")

    def statistics(self, type_statistic: statistic_type) -> dict:

        return type_statistic.run_statistic(self.clients)
