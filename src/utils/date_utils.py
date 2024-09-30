from datetime import datetime


class DateUtil:
    @staticmethod
    def get_today(format: str = "%Y-%m-%d") -> str:
        return datetime.now().strftime(format=format)
