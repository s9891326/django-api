import datetime


def get_date_time_str(date: datetime.datetime):
    return date.strftime('%Y/%m/%d %H:%M:%S')
