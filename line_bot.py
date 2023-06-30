from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(
    os.environ['q50Ea4vymjJI7KXZ1hIuv0q/nFtZQZcoDAsfffuDHZG1rerRg+DlkYaR6FezajKR4s7RQO9Y9NWzjD1XykwE2HNlIImT3KuH6bjn3RN2A5azvH/Q5aCs6yfFS1mH53eg9kj3GRxr+yuDmGARCzdW4AdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['2f6d1344222cad629ed491b89d02a6be'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
