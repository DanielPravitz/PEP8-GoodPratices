from base_queue import BaseQueue


class PriorityQueue(BaseQueue):

    def password_generator(self) -> None:
        self.password = f"PR{self.code}"

    def call_client(self, cashier: int) -> str:
        actual_client: str = self.queue.pop(0)
        self.clients.append(actual_client)

        return(f"Client number {actual_client} , go to cashier {cashier}")

    def statistics(self, date: str, agency: int, flag: str) -> dict:
        if flag != "detail":
            statistics = {f"{agency}-{date}": len(self.clients)}
        else:
            statistics = {}
            statistics["date"] = date
            statistics["agency"] = agency
            statistics["clients"] = self.clients
            statistics["total clients"] = len(self.clients)

        return statistics
