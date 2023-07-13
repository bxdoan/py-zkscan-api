from datetime import datetime
import requests

from py_zkscan_api.constants import EXPLORER_URL, DATE_FORMAT


class Explorers(object):

    def __init__(self, to_date = None, **kwargs):
        self.to_date = to_date or f'{datetime.now().strftime(DATE_FORMAT)[:-3]}Z'
        self.page_size = kwargs.get('page_size') or 10
        self.page = kwargs.get('page') or 1

    def get_blocks(self):
        params = {
            'page': 1,
            'pageSize': 10,
            'toDate': self.to_date,
        }
        resp = requests.get(f'{EXPLORER_URL}/blocks', params=params)
        if resp.status_code == 200:
            res = resp.json().get('items')
        else:
            res = []
        return res

    def get_last_block(self):
        blocks = self.get_blocks()
        if blocks:
            return blocks[0]
        return None

    def get_block_by_number(self, number : int = 0) -> list or None:
        if not number:
            return None
        params = {
            'blockNumber': number,
            'pageSize': self.page_size,
            'page': self.page,
            'toDate': self.to_date,
        }
        resp = requests.get(f'{EXPLORER_URL}/transactions', params=params)
        if resp.status_code == 200:
            res = resp.json().get('items')
        else:
            res = None
        return res

    def get_block_by_hash(self, block_hash : str = ''):
        if not block_hash:
            return None
        params = {
            'blockHash': str(block_hash),
            'pageSize': 10,
            'page': 1,
            'toDate': self.to_date,
        }
        resp = requests.get(f'{EXPLORER_URL}/transactions', params=params)
        if resp.status_code == 200:
            res = resp.json().get('items')
        else:
            res = None
        return res
