from typing import Dict, List, Union


class StatisticDetailed:

    def __init__(self, date: str, agency: int) -> None:
        super().__init__()

        self.date = date
        self.agency = agency

    def run_statistic(self, total_clients: List[str]) -> dict:

        statistics: Dict[str, Union[List[str], str, int]] = {}

        statistics["date"] = self.date
        statistics["agency"] = self.agency
        statistics["clients"] = total_clients
        statistics["total clients"] = len(total_clients)

        return statistics
