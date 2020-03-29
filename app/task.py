"""
    Wrapper around the Item that is returned from get_by_id that is json-
    serializable.
"""
from datetime import datetime, timezone
import dateutil.parser

def parse(i):
    d = {}
    d['id'] = i['id']
    d['content'] = i['content']
    d['checked'] = i['checked']
    d['is_deleted'] = i['is_deleted']
    d['due'] = i['due']
    d['priority'] = i['priority']
    if i['due']:
        d['dcdiff'] = str((parse_date(i['date_completed']) - parse_date(i['due']['date'])).total_seconds())
    else:
        d['dcdiff'] = ''
    return d

def parse_date(d):
    return dateutil.parser.parse(d).astimezone(timezone.utc)

def difference_from_today(due_date_utc):
    return datetime.now(timezone.utc) - parse_date(due_date_utc)

def item_completed_since(item, days):
    return item['checked'] and item['date_completed'] and difference_from_today(item['date_completed']).days < days

def is_item_completable(item):
    return not item['is_deleted'] and not item['checked']

def due_today(item):
    return item['due_date_utc'] is not None and is_today(item['due_date_utc'])

def is_today(due_date_utc):
    """ returns true if the date (in utc format) occurs today. """
    return difference_from_today(due_date_utc).days == 0

