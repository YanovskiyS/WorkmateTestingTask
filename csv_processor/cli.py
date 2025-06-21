import argparse

from csv_processor.processor import (
    read_csv,
    filter_data,
    aggregate_data,
    display_result,
)
from csv_processor.utils import parse_condition, aggregation_parse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Process CSV files with filtering and aggregation"
    )

    parser.add_argument("--file", required=True, help="Path to the CSV file")

    parser.add_argument(
        "--where",
        help="Filter condition in format 'column=value' or 'column>value' etc.",
    )

    parser.add_argument("--aggregate", help="Aggregation in format 'column=operation'")

    return parser.parse_args()


def main():
    args = parse_arguments()
    data = read_csv(args.file)

    if args.where:
        column, operator, value = parse_condition(args.where)
        result = filter_data(data, column, operator, value)
        if args.aggregate:
            column, operator = aggregation_parse(args.aggregate)
            result = aggregate_data(result, column, operator)
            display_result(result, True)
        else:
            display_result(result)

    elif args.aggregate:
        column, operator = aggregation_parse(args.aggregate)
        result = aggregate_data(data, column, operator)
        display_result(result, True)

    else:
        display_result(data)
