import datetime


def _convert_date_to_str(date: datetime.datetime) -> str:
    return date.strftime('%Y-%m-%dT%H:%M:%S.%f')
