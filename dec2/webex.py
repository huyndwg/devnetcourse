from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return "Helo ong gia ngheo kho"
    elif request.method == "POST":
        data = request.get_json()
        print(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)