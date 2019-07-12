import json
from typing import Dict, List

import requests

from .wgc_constants import WoTPAPIRealms
from .wgc_spa import sort_by_realms

class WoTPAPI(object):


    URL_WOT_ACCOUNT_INFO = 'wot/account/info/'

    @staticmethod
    def get_account_info(account_ids : List[int]) -> Dict[str, Dict[int, object]]:

        info = dict()

        for realm_id, realm_spa_ids in sort_by_realms(account_ids).items():
            params = dict()
            params['application_id'] = WoTPAPIRealms[realm_id]['client_id']
            params['account_id'] = str.join(',', [str(spa_id) for spa_id in realm_spa_ids])

            url = 'https://%s/%s' % (WoTPAPIRealms['RU']['host'], WoTPAPI.URL_WOT_ACCOUNT_INFO)
            
            response = requests.get(url, params = params)
            response_json = json.loads(response.text)
            info[realm_id] = response_json['data']

        return info
