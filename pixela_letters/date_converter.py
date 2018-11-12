from datetime import datetime, timedelta
from typing import Optional


def parse_from_ymd_string(ymd: str) -> Optional[datetime]:
    try:
        return datetime.strptime(ymd, '%Y%m%d')
    except ValueError:
        return None


def find_last_monday(source: datetime) -> datetime:
    return source - timedelta(days=source.weekday())
