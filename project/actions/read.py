
from datetime import datetime
import os
import csv
from .options import Option_csv_dict as OPTIONS


class File_csv(OPTIONS):
    """
        This class acept two init arguments, first with the
        list paths or a single path of directory, and second,
        with de list of the csv format files, such as exce, csv
        or similar.
    """

    def __init__(self, path_file: str | list, csv_dict=None) -> None:
        super().__init__(csv_dict)
        self.__path_file = path_file
        self.csv_dict = self.merge_csv()

    @property
    def path_file_show(self) -> str | list:
        return self.__path_file

    def add_path_file(self, path: str | tuple) -> None:
        if type(self.__path_file) is str:
            if type(path) == str:
                self.__path_file = [self.__path_file, path]
            else:
                self.__path_file = [self.__path_file]
                self.__path_file.extend(path)
        else:
            if type(path) == str:
                self.__path_file = [self.__path_file, path]
            else:
                self.__path_file.extend(path)

    def merge_csv(self) -> list:
        """
            You can to merge any csv files in a simple file.
            This function return a list with dictionaries.
            You can to convert the result in a csv file with the
            convert_csv method.
        """

        dir_paths = self.path_file_show

        if type(dir_paths) == str:
            dir_paths = [self.path_file_show]
        elif type(dir_paths) != list:
            raise Exception("Error, path list is not a list or str.")

        overall_list = []
        for route in dir_paths:
            try:
                directory = os.scandir(route)
            except FileNotFoundError as Error:
                print(f'Path file not found. Validate route: {route}')
                return Error

            merge_files = []
            counter_files = 0
            for file in directory:
                if file.name.endswith('csv'):
                    with open(file.path, 'r', encoding='utf-8') as csv_file:
                        csv_converter = csv.DictReader(csv_file)
                        merge_files.extend(list(csv_converter))
                        counter_files += 1
                        csv_file.close()
            overall_list.extend(merge_files)
        return overall_list

    @classmethod
    def converto_csv(self, data: list[dict] | tuple[dict], destination_route: str) -> bool:

        init_time = datetime.now().microsecond

        fieldnames = []
        for key in data[0]:
            fieldnames.append(key)

        file_name = f'combinedcsvfile-{str(datetime.now().date())+"_"+str(datetime.now().microsecond)}.csv'

        try:
            path_save_file = f"{destination_route}/{file_name}"
            with open(path_save_file, 'w') as document:
                file_write = csv.DictWriter(document, fieldnames=fieldnames)
                file_write.writeheader()
                file_write.writerows(tuple(data))
                document.close()
                print(file_name +
                      f" file has been created in route {path_save_file}")
                print("Task end in : " + str((datetime.now().microsecond -
                                              init_time)/1000000) + " seconds.")
                return True
        except Exception as exc:
            print(exc)
            raise Exception("Validate route and data.")
