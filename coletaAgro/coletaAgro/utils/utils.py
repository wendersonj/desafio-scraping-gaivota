from datetime import date, datetime


def convert_str_to_date(value: str) -> date:
    return date(datetime.strptime(value, '%d/%m/%Y'))