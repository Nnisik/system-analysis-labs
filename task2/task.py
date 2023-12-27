import csv


def find_max_element(data):
    return max(map(max, data))

def get_child_element(data, x):
    result = []
    for elem in data:
        if elem[0] == x:
            result.append(elem[1])
    return result

def get_parent_element(data, x):
    for elem in data:
        if elem[1] == x:
            return list(elem[0])
    return []

def task(data: list):
    result = []

    for i in range(find_max_element(data)):
        child_elements = get_child_element(data, i + 1)
        parent_elemet = get_parent_element(data, i + 1)
        r1 = len(child_elements)
        r2 = len(parent_elemet)
        r3 = 0

        for elem in child_elements:
            r3 += len(get_child_element(data, elem))
        
        if not r2:
            r4 = 0
            r5 = 0
        else:
            r4 = len(get_parent_element(data, parent_elemet[0]))
            r5 = max(len(get_child_element(data, parent_elemet[0])))
        result.append(list(r1, r2, r3, r4, r5))
    return result


if __name__ == "__main__":
    # read csv file
    with open("./task2.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
    
    with open("./result-csv.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(task(data))