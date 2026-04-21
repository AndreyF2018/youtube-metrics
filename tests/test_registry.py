import pytest
from app.reports.registry import get_report


def test_get_valid_report():
    report = get_report("clickbait")
    assert report is not None


def test_get_invalid_report():
    with pytest.raises(ValueError):
        get_report("unknown")