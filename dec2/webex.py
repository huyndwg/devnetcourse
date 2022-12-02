from flask import Flask, request
from api import get_messages, post_messages
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return "Helo ong gia ngheo kho"
    elif request.method == "POST":
        data = request.get_json()
        roomId = data['data']['roomId']
        msgId = data['data']['id']
        print(json.dumps(data, indent=3))
        print(roomId)

        usr_msg = get_messages(msgId)
        print(usr_msg)

        bot_send_msg = f"Message sent: {usr_msg}"
        post_messages(roomId=roomId, text_msg=usr_msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)