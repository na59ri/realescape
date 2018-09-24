from linebot.models import (
    # メッセージのイベント
    MessageEvent,
    # 友だち追加、削除
    FollowEvent, UnfollowEvent,
    # ビーコン取得
    BeaconEvent
)

from start import startFactory
from tutorial import tutorialFactory
from game import gameFactory
from end import endFactory

# 独自ライブラリ呼び出し
import sys
sys.path.append(os.getcwd() + '/control')
from lineBotController import LineBotController
from kintoneController import kintoneController


class state(object):

    factoryArray = {START: startFactory, TUTORIAL: tutorialFactory,
                    GAME: gameFactory, END: endFactory}

    START = 1
    TUTORIAL = START + 1
    GAME = TUTORIAL + 1
    END = GAME + 1

    def action(self, messageEvent, event):
        print('state state start')
        print(kintoneController.getState(event.userId))
