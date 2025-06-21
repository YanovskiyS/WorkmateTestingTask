def convert_value(value: str):
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except ValueError:
        return value


def parse_condition(condition: str) -> tuple:
    operators = [">", "<", "="]

    for operator in operators:
        if operator in condition:
            parts = condition.split(operator)
            if len(parts) == 2:
                column = parts[0]
                value = convert_value(parts[1])
                return column, operator, value
    raise ValueError(f"Invalid condition format: {condition}")


def aggregation_parse(aggregation: str):
    if "=" not in aggregation:
        raise ValueError("Aggregation must be in format 'column=operation'")
    column, operation = aggregation.split("=")
    return column.strip(), operation.strip()
