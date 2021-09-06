from typing import Dict, List, Union


class StatisticSummarized:

    def __init__(self, date: str, agency: int) -> None:
        super().__init__()

        self.date = date
        self.agency = agency

    def run_statistic(self, total_clients: List[str]) -> dict:

        statistics: Dict[str, Union[List[str], str, int]] = {}

        statistics[f"{self.agency}-{self.date}"] = len(total_clients)

        return statistics
