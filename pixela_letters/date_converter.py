from datetime import datetime, timedelta
from typing import Optional


def parse_from_ymd_string(ymd: str) -> Optional[datetime]:
    try:
        return datetime.strptime(ymd, "%Y%m%d")
    except ValueError:
        return None


def convert_to_ymd_string(target: datetime) -> str:
    return "{0:%Y%m%d}".format(target)


def find_last_start_date(source: datetime) -> datetime:
    return source - timedelta(days=source.weekday() + 1)
