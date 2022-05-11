class Option_csv_dict:
    def __init__(self, csv_dict: list[dict] | tuple[dict]) -> None:
        self.csv_dict = csv_dict

    def organize_by_AZ(self, field_order="Score"):
        csv_order = sorted(
            self.csv_dict, key=lambda x: x[field_order], reverse=True)
        self.csv_dict = csv_order
        return csv_order

    def organize_by_ZA(self, field_order="Score"):
        csv_order = sorted(
            self.csv_dict, key=lambda x: x[field_order], reverse=False)
        self.csv_dict = csv_order
        return csv_order

    def unique_registers(self) -> list:
        def combine_name(x):
            new_dic = {}
            full_name = x['First Name'] + " " + x['Last Name']
            x['Full Name'] = full_name.strip().title()

            for key in x:
                if key not in ['First Name', 'Last Name']:
                    new_dic[key] = x[key]
            return new_dic

        data = list(map(combine_name, self.csv_dict))

        result = {}
        for student in data:
            if student['Full Name'] in result.keys():
                result[student['Full Name']] += int(student['Score'])
            else:
                result[student['Full Name']] = int(student['Score'])

        for x in data:
            for y in result:
                if x['Full Name'] == y:
                    x['Score'] = result[y]

        ides = []
        unique_values = []
        for register in data:
            if register['Full Name'] not in ides:
                ides.append(register['Full Name'])
                unique_values.append(register)

        self.csv_dict = unique_values

        return (unique_values, result)
