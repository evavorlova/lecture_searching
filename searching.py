import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)


def main():
    pass

def read_data(sequential,field):
    with open("sequential.json", mode="r") as file:
        allowed_keys = json.load(file)["allowed_keys"]
    if field not in allowed_keys:
        return None

    with open(file_name,"r") as file:
        data = json.load(file)
    return data.get(field, None)

def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    print("Sequential Data:", sequential_data)

def linear_search(sequence,target):
    positions = []
    count = 0
    for i, num in enumerate(sequence):
        if num == target:
            positions.append(i)
            count += 1

    return {"positions": positions, "count": count}

def pattern_search(sequence, target):
    positions = set()
    seq_length = len(sequence)
    pattern_length = len(pattern)
    for i in range(seq_length - pattern_length + 1):
        if sequence[i:i + pattern_length] == pattern:
            positions.add(i)
    return positions


if __name__ == '__main__':
    main()