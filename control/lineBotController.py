from os
from flask import request
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    # メッセージのイベント
    MessageEvent,
    # 友だち追加、削除
    FollowEvent, UnfollowEvent,
    # ビーコン取得
    BeaconEvent,
    # テキストのメッセージ
    TextMessage,
    # テキストの返信用フォーマット
    TextSendMessage,
)

# LINE Access Token
LINE_BOT_ACCESS_TOKEN = os.environ["LINE_BOT_ACCESS_TOKEN"]
# LINE Channel Secret
LINE_BOT_SECRET_KEY = os.environ["LINE_BOT_SECRET_KEY"]

line_bot_api = LineBotApi(LINE_BOT_ACCESS_TOKEN)
handler = WebhookHandler(LINE_BOT_SECRET_KEY)


class LineBotController:

    def action(request):

        print("LineBotController action stary")
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']

        # get request body as text
        body = request.get_data(as_text=True)

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

# ----------------------------------------------
# メッセージを受信


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("MessageEvent start")

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))


# ----------------------------------------------
# 友だち追加イベントを受信

@handler.add(FollowEvent)
def handle_follow(event):
    print("FollowEvent start")

# ----------------------------------------------
# 友だち解除イベントを受信


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print("UnfollowEvent start")

# ----------------------------------------------
# ビーコンイベントを受信


@handler.add(BeaconEvent)
def handle_beacon(event):
    print("BeaconEvent start")
