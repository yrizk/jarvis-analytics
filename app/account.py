"""
All functions related to interacting with todoist account.
"""

from todoist.api import TodoistAPI

def get_api(client_id='81acb5be0fdf242ff6af5bd6cf1f56a66225a861'):
    """ Create an api that is in sync with todoist. """
    api = TodoistAPI(client_id)
    api.sync()
    return api
