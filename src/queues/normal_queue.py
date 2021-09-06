from queues.base_queue import BaseQueue
from constants.constants import NORMAL_CODE


class NormalQueue(BaseQueue):

    def password_generator(self) -> None:
        self.password = f"${NORMAL_CODE}{self.code}"

    def call_client(self, cashier: int) -> str:
        actual_client: str = self.queue.pop(0)
        self.clients.append(actual_client)
        return(f"Client number {actual_client} , go to cashier {cashier}")
