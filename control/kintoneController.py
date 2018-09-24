import os
from kintone_sdk4python import Kintone

# 独自ライブラリ呼び出し
import sys
sys.path.append(os.getcwd() + '/state')
from state import state

kintone = Kintone()
kintone.set_domain(os.environ["KINTONE_DOMAIN"])
# kintone.set_token_auth('api-token')

tokenArray = {2: os.environ["KINTONE_REGISTER_TOKEN"],
              3: os.environ["KINTONE_CONNECT_TOKEN"],
              4: os.environ["KINTONE_SCENARIO_TOKEN"],
              5: os.environ["KINTONE_HINT_TOKEN"],
              6: os.environ["KINTONE_USER_TOKEN"],
              7: os.environ["KINTONE_USERSCENARIO_TOKEN"]
              }


class kintoneController:

    def getState(userId):
        appId = 2
        kintone.set_token_auth(tokenArray[appId])
        #        query = "groupId = \"" + groupId + "\" and userId = \"" + userId + "\""
        query = 'userId="' + userId
        ret = kintone.get_records(appId, query, [hwid], True, '')
        print(ret)
        return state.START
