from flask import Flask
import api

app = Flask(__name__)

@app.route("/")
def api_return():
    return api.json_test()

if __name__ == "__main__":
    app.run()