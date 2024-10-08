from datetime import datetime


class DateUtil:
    @staticmethod
    def get_today(format: str = "%Y-%m-%d") -> str:
        return datetime.now().strftime(format=format)

    @staticmethod
    def split_date(date: str) -> tuple:
        return tuple(map(int, date.split("-")))
