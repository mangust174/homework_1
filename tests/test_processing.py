import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_exec(sample_operations):
    filtered = filter_by_state(sample_operations, "EXECUTED")
    assert all(op["state"] == "EXECUTED" for op in filtered)
    assert len(filtered) == 2


def test_filter_by_state_not_found(sample_operations):
    assert filter_by_state(sample_operations, "UNKNOWN") == []


@pytest.mark.parametrize("reverse", [True, False])
def test_sort_by_date(sample_operations, reverse):
    sorted_ops = sort_by_date(sample_operations, reverse=reverse)
    dates = [op["date"] for op in sorted_ops]
    ordered = sorted(dates, reverse=reverse)
    assert dates == ordered


def test_sort_by_date_stability_equal(sample_operations):
    dup = sample_operations + [sample_operations[0].copy()]
    result = sort_by_date(dup, reverse=False)
    assert len(result) == len(dup)