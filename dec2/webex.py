from flask import Flask, request
from api import get_message, post_message, get_bot_id
import json


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return "Helo ong gia ngheo kho"
    elif request.method == "POST":
        data = request.get_json()

        if get_bot_id() == data['data']['personId']:
            print("Ignore message from botself")
        else:
            roomId = data['data']['roomId']
            msgId = data['data']['id']
            print(json.dumps(data, indent=3))

            bot_msg = f"Message received: {get_message(msgId)}"
            post_message(roomId=roomId, text_msg=bot_msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969, debug=False)