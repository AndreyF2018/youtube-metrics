from abc import ABC, abstractmethod
from typing import List
from app.models import Video


class BaseReport(ABC):

    @abstractmethod
    def generate(self, videos: List[Video]) -> List[Video]:
        pass