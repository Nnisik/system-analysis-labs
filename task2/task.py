import csv


def task(csv_string: str) -> str:
    reader = csv.reader(csv_string)
    for row in reader:
        print(row)
    # TODO: read data from the file and convert it into a matrix
    # TODO: understand the assignment
    pass

if __name__ == "__main__":
    with open("./task2.csv", "r") as csv_file:
        task(csv_file)