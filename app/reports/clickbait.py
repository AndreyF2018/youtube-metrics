from typing import List
from app.models import Video
from .base import BaseReport


class ClickbaitReport(BaseReport):

    def generate(self, videos: List[Video]) -> List[Video]:
        result = [
            v for v in videos
            if v.ctr > 15 and v.retention_rate < 40
        ]

        return sorted(result, key=lambda x: x.ctr, reverse=True)