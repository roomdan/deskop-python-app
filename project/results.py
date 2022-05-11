from .actions.read import File_csv
from .main.settings import CSV_RESULTS


class Results(CSV_RESULTS):

    winners_dict = {}

    def __init__(self, route: str) -> None:
        self.route = route
        self.__result_data = self.results()
        super().__init__()

    def results(self):
        read_file = File_csv(self.route)
        read_file.merge_csv()
        data = read_file.unique_registers()
        result = read_file.organize_by_AZ(field_order="Score")
        self.winners_dict = data[1]
        return result

    def get_winners(self, limit: int = 3) -> list:
        return self.__result_data[0:limit]

    @property
    def get_min_result(self) -> dict:
        return self.__result_data[-1]

    @property
    def get_max_result(self) -> dict:
        return self.__result_data[0]

    @property
    def get_general_results(self) -> list[dict]:
        return self.__result_data

    def get_average_result(self):
        return super().get_average_result()

    def get_data_by_name(self, name: str = "") -> dict:
        name = name.lower()
        results = []
        for student in self.__result_data:
            if student['Full Name'].lower().find(name) >= 0:
                results.append(student)
        return results
