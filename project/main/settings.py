from abc import ABC, abstractmethod


class CSV_RESULTS(ABC):

    @abstractmethod
    def get_winners(self):
        pass

    @abstractmethod
    def get_max_result(self):
        pass

    @abstractmethod
    def get_min_result(self):
        pass

    @abstractmethod
    def get_average_result(self):
        pass

    @abstractmethod
    def get_general_results(self):
        pass
