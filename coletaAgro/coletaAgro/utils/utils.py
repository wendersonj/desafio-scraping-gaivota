from datetime import date, datetime


def convert_str_to_date(value: str) -> date:
    return datetime.strptime(value, '%d/%m/%Y').date()
