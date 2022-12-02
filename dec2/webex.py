from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "App run on port 6969"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)