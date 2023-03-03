from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

#client = MongoClient("mongodb://mongodb_tp6:27017/")
client = MongoClient("mongodb://tp6-mongodb-1:27017/")

db = client["films"]

collection = db["favoris"]

@app.route("/")
def index():
    data = collection.find()
    rend = ""
    for i in range(3):
        rend += "Film " + str(i) + " : "
        rend += str(data[i])
        rend += "<br\>"
    return rend

@app.route("/tp6")
def show_content():
    with open("/app/text/content.txt", "r") as f:
        content = f.read()
    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
