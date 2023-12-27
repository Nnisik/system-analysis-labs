import csv
import math

def calculate_entropy(n: int, k: int, l):
    H = 0
    for i in range(1, n):
        for k in range(1, k):
            H += (l/(n - 1)) * math.log10(l/(n - 1))
    return H * (-1)

def task(csv_path: str) -> None:
    entropy = 0

    # read csv file
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        len_data = len(data)
    
    for row in data:
        for elem in row:
            entropy += calculate_entropy(elem, len_data)
    
    return entropy


if __name__ == "__main__":
    file_path = "./task3.csv"
    print(task(file_path))