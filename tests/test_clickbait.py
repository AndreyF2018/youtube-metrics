import pytest
from app.models import Video
from app.reports.clickbait import ClickbaitReport


@pytest.fixture
def sample_videos():
    return [
        Video("Good", 20, 30),     # подходит
        Video("Low CTR", 10, 30),  # не подходит
        Video("High Ret", 20, 50), # не подходит
        Video("Best", 30, 20),     # подходит
    ]


def test_clickbait_filter(sample_videos):
    report = ClickbaitReport()
    result = report.generate(sample_videos)

    titles = [v.title for v in result]

    assert titles == ["Best", "Good"]


@pytest.mark.parametrize(
    "ctr, retention, expected",
    [
        (16, 39, True),
        (15, 39, False),
        (16, 40, False),
        (10, 20, False),
    ]
)
def test_clickbait_conditions(ctr, retention, expected):
    report = ClickbaitReport()
    video = Video("Test", ctr, retention)

    result = report.generate([video])

    assert (len(result) == 1) == expected