from tabulate import tabulate
from app.models import Video


def print_table(videos: list[Video]):
    table = [
        [v.title, v.ctr, v.retention_rate]
        for v in videos
    ]

    print(tabulate(
        table,
        headers=["title", "ctr", "retention_rate"],
        tablefmt="grid"
    ))