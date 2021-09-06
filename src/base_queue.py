import abc
from typing import List

from constants import DEFAULT_MAX_SIZE, DEFAULT_MIN_SIZE


class BaseQueue(metaclass=abc.ABCMeta):
    code: int = 0
    queue: List[str] = []
    clients: List[str] = []
    password: str = ""

    def reset_queue(self) -> None:
        if self.code >= DEFAULT_MAX_SIZE:
            self.code = DEFAULT_MIN_SIZE
        else:
            self.code += 1

    def client_insert(self):
        self.queue.append(self.password)

    def update_queue(self):
        self.reset_queue()
        self.password_generator()
        self.client_insert()

    @abc.abstractmethod
    def password_generator(self):
        ...

    @abc.abstractmethod
    def call_client(self, cashier: int) -> str:
        ...
