import csv

def parse_data(csv_data, row_number, element_number) -> bool:
    if len(csv_data) >= row_number:
        print("Row doesn't exist")
        return False
    elif len(csv_data[row_number]) >= element_number:
        print("Element doesn't exist")
        return False
    else:
        print(*csv_data[row_number][element_number])
        return True

if __name__ == "__main__":
    input_data = input("Путь до файла, номера строки и столбца: ")
    file_path, row_number, column_number = input_data.split(",")

    row_number -= 1
    column_number -= 1

    with open(file_path, "r") as file:
        data_array = []
        for row in file:
            data_array.append(row.split(","))
            data_array[-1].pop(-1)
        parse_data(data_array, row_number, column_number)