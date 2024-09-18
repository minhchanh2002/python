from flask import Flask
import pandas as pd

app = Flask(__name__)
@app.route("/churn_count")
def churn_count():
    df = pd.read_csv('Telco-Customer-Churn.csv')
    result = df['Churn'].to_json()
    return result

# Chạy chương trình chính
if __name__ == "__main__":
    app.run()