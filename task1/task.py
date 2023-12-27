import csv

def parse_data(csv_data, row_number, element_number) -> bool:
    if row_number < 0 or element_number < 0:
        print("Negative index")
        return
    
    if len(csv_data) >= row_number:
        print("Row doesn't exist")
        return
    
    if len(csv_data[row_number]) >= element_number:
        print("Element doesn't exist")
        return
    
    else:
        print(*csv_data[row_number][element_number])
        return

if __name__ == "__main__":
    file_path = "./example.csv"
    row_number, column_number = int(input().split(","))

    row_number -= 1
    column_number -= 1

    with open(file_path, "r") as file:
        data_array = []
        for row in file:
            data_array.append(row.split(","))
            data_array[-1].pop(-1)
        parse_data(data_array, row_number, column_number)