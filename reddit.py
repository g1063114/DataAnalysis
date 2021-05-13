import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
url = 'https://www.reddit.com'

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("Reddit")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/read", methods=['POST','GET'])
def read():
    items=[]
    if request.method == 'GET':
        for i in subreddits:
            if request.args.get(i) != None:
                reddit_url = requests.get(url+f"/r/{i}/top/?t=month",headers=headers)
                content = BeautifulSoup(reddit_url.text,"html.parser")
                items = content.find_all("a",{"data-click-id":"body"})

                print(items)
             
    return render_template("read.html")



app.run()