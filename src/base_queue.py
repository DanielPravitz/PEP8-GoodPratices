import abc


class BaseQueue(metaclass=abc.ABCMeta):
    code: int = 0
    queue: list = []
    clients: list = []
    password: str = " "

    def reset_queue(self) -> None:
        if self.code >= 200:
            self.code = 0
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
