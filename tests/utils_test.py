import pytest

from csv_processor.utils import parse_condition, aggregation_parse, convert_value


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone", "price": "999", "rating": "4.9"},
        {"name": "galaxy", "price": "1199", "rating": "4.8"},
        {"name": "redmi", "price": "199", "rating": "4.6"},
        {"name": "poco", "price": "299", "rating": "4.4"},
    ]


def test_parse_condition():
    assert parse_condition("brand=apple") == ("brand", "=", "apple")
    assert parse_condition("price>500") == ("price", ">", 500)


def test_aggregation_parse():
    assert aggregation_parse("price=avg") == ("price", "avg")
    assert aggregation_parse("rating=min") == ("rating", "min")


def test_convert_value():
    assert convert_value("15") == 15
    assert convert_value("apple") == "apple"
