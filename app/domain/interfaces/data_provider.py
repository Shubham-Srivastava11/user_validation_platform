from abc import ABC, abstractmethod

class DataProvider(ABC):

    @abstractmethod
    def fetch_user(self, linkedin: str) -> dict:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
