import os
from flask import request
from cek import Clova

# clova application_id
application_id = os.environ["APPLICATION_ID"]
# Set debug_mode=True if you are testing your extension. If True, this disables request verification
clova = Clova(application_id=application_id,
              default_language="ja", debug_mode=False)

hintList = ['モンゲー', '非日常', 'まり、、、なんとか']


class LineBotController:

    def action(request):

        resp = clova.route(request.data, request.headers)
        resp = jsonify(resp)
        # make sure we have correct Content-Type that CEK expects
        resp.headers['Content-Type'] = 'application/json;charset-UTF-8'
        return resp


# ----------------------------------------------
# メッセージを受信
@clova.handle.launch
def launch_request_handler(clova_request):
    return clova.response("こんにちは世界。スキルを起動します")


@clova.handle.default
def default_handler(clova_request):
    return clova.response("もう一度お願いします")


@clova.handle.intent('HintIntent')
def hint_handler(clova_request):
    quantity = clova_request.slot_value('quantity')
    orientation = clova_request.slot_value('orientation')
    response = None
    reprompt = None
    message = 'ヒントはないぜよ'
    end_session = True
    if quantity is not None:
        if quantity < len(hintList) - 1:
            message = hintList[quantity - 1]

    response = response_builder.simple_speech_text(
        message, end_session=end_session)

    return response
