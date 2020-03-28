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
    due_date = ''
    if i['due'] is None:
        due_date = str(datetime.now(timezone.utc))
    d['dcdiff'] = str((parse_date(i['date_completed']) - parse_date(due_date)).total_seconds())
    return d

#TODO: might I need to do something else in the future? Can i throw out items have
# a difference of < 1 second?
def parse_date(d):
    try:
        return dateutil.parser.parse(d)
    except ValueError:
        return datetime.now(timezone.utc)

def is_valid(t):
    return t['dcdiff'] > 1

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

