import pytest

from csv_processor.processor import filter_data, aggregate_data

@pytest.fixture
def sample_data():
    return [
        {"name": "iphone", "price": "999", "rating": "4.9"},
        {"name": "galaxy", "price": "1199", "rating": "4.8"},
        {"name": "redmi", "price": "199", "rating": "4.6"},
        {"name": "poco", "price": "299", "rating": "4.4"},
    ]


def test_filter_data_equals(sample_data):
    result = filter_data(sample_data, "name", "=", "iphone")
    assert len(result) == 1
    assert result[0]["name"] == "iphone"


def test_filter_data_greater_than(sample_data):
    result = filter_data(sample_data, "rating", ">", "4.4")
    assert len(result) == 3
    assert all(float(item["rating"]) > 4.4 for item in result)


def test_filter_data_less_than(sample_data):
    result = filter_data(sample_data, "price", "<", "1199")
    assert len(result) == 3
    assert all(float(item["price"]) < 1199 for item in result)


def test_aggregate_avg(sample_data):
    result = aggregate_data(sample_data, "rating", "avg")
    assert result["avg"] == pytest.approx((4.4 + 4.6 + 4.8 + 4.9) / 4)


def test_aggregate_min(sample_data):
    result = aggregate_data(sample_data, "price", "min")
    assert result["min"] == 199