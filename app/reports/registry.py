from .clickbait import ClickbaitReport

REPORTS = {
    "clickbait": ClickbaitReport,
}


def get_report(name: str):
    if name not in REPORTS:
        raise ValueError(f"Unknown report: {name}")
    return REPORTS[name]()