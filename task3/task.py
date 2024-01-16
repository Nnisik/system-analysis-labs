import csv
import math

def calculate_entropy(n: int, k: int, l):
    H = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            H += (l/(n - k)) * math.log10(l/(n * k))
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
            entropy += calculate_entropy(len(row), len_data, elem) 
    
    return entropy


if __name__ == "__main__": 
    file_path = "./task3.csv"
    print(task(file_path))
