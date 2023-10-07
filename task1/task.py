import csv

def parse_data(row_data, element_number):
    row = row_data.split(",")
    if len(row) > element_number:
        error_catch = True
        return "InputError: column number is bigger than number of columns"
    else:
        return row[element_number]

if __name__ == "__main__":
    input_data = input("Путь до файла, номера строки и столбца: ")
    file_path, row_number, column_number = input_data.split(",")

    error_catch = False

    row_number -= 1
    column_number -= 1

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        current_row = 0
        for row in file:
            if current_row == row_number:
                print(parse_data(row, column_number))
                break
            current_row += 1