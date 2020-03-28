import task
from account import get_api

def get_full_name():
    return get_api().state['user']['full_name']

def completed_item_count_since():
    api = get_api()
    completed_items = {}
    for project in api.state['projects']:
        items = []
        for item in api.items.get_completed(project['id']):
            if task.item_completed_since(item, 30):
                i = api.items.get_by_id(item['id'])
                t = task.parse(i)
                if task.is_valid(t):
                    items.append(t)
        if len(items) > 0:
            completed_items[project['name']] = items
    return completed_items

def group_by_priority(data):
    result = {}
    for k,v in data.items():
        for item in v:
            p = item['priority']
            if p not in result:
                result[p] = []
            else:
                result[p].append(item)
    return result
