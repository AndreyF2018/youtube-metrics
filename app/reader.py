import csv
from typing import List
from .models import Video


def read_videos(file_path: str) -> List[Video]:
    videos = []

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            videos.append(
                Video(
                    title=row["title"],
                    ctr=float(row["ctr"]),
                    retention_rate=float(row["retention_rate"]),
                )
            )

    return videos


def read_multiple(files: list[str]) -> list[Video]:
    all_videos = []
    for file in files:
        all_videos.extend(read_videos(file))
    return all_videos