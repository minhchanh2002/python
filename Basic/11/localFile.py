from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
@app.route("/local_file")
def local_file():
    with open('local file.txt', 'r', encoding = 'utf-8') as file:
        content = file.readlines()

    result = {"lines": content}
    return jsonify(result)

if __name__ == "__main__":
    app.run()