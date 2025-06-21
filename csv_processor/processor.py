import csv
from tabulate import tabulate
from typing import Dict, List, Union, Optional


def read_csv(file_path: str) -> List[Dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def filter_data(
    data: List[Dict], column: str, operator: str, value: Union[str, int, float]
) -> list[Dict]:
    filtered = []
    for row in data:
        column_value = row.get(column)
        if column_value is None:
            continue

        try:
            float_column_value = float(column_value)
            float_value = (
                float(value) if isinstance(value, (int, float)) else float(value)
            )

            if operator == "=" and float_column_value == float_value:
                filtered.append(row)
            elif operator == ">" and float_column_value > float_value:
                filtered.append(row)
            elif operator == "<" and float_column_value < float_value:
                filtered.append(row)
        except (ValueError, TypeError):
            if operator == "=" and str(column_value) == str(value):
                filtered.append(row)
            elif operator == ">" and str(column_value) > str(value):
                filtered.append(row)
            elif operator == "<" and str(column_value) < str(value):
                filtered.append(row)
    return filtered


def aggregate_data(
    data: List[Dict], column: str, operation: str
) -> Optional[Union[int, float, Dict]]:
    result = []
    for row in data:
        try:
            value = float(row[column])
            result.append(value)
        except (ValueError, TypeError):
            return None

    if operation == "avg":
        return {operation: round(sum(result) / len(result), 2)}
    elif operation == "max":
        return {operation: max(result)}
    elif operation == "min":
        return {operation: min(result)}


def display_result(data_for_display, is_aggregation=False):
    if is_aggregation:
        print(tabulate([data_for_display], headers="keys", tablefmt="github"))

    else:
        print(tabulate(data_for_display, headers="keys", tablefmt="github"))
