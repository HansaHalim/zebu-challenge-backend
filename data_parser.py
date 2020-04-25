import csv

data_path = "./data/"

def get_file_as_dct(file_path):
    full_file_path = data_path + file_path

    data = []

    with open(full_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        id_to_col_name = None
        for line_count, row in enumerate(csv_reader):
            if line_count == 0:
                id_to_col_name = row
            else:
                entry = {}
                for col, v in enumerate(row):
                    col_name = id_to_col_name[col]
                    entry[col_name] = v

                data.append(entry)
    return data

def get_item_data(filename):
    items = get_file_as_dct(filename)
    return items
