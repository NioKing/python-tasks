from datetime import datetime, timedelta

def date_in_future(days):
    if(isinstance(days, int)):
        new_date = datetime.now() + timedelta(days=days)
        return new_date.strftime('%d-%m-%Y %H:%M:%S')
    else:
        return datetime.strftime('%d-%m-%Y %H:%M:%S')

date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня