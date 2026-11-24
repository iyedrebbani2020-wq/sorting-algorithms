import random
import csv
import os

def generate_array(size: int, data_type: str = "random", seed: int = 42) -> list:
    random.seed(seed)
    if data_type == "random":
        return [random.randint(0, size * 10) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse":
        return list(range(size, 0, -1))
    elif data_type == "duplicates":
        return [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
    else:
        raise ValueError("Unknown data type")

def export_to_csv(filename: str, rows: list, headers: list):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

