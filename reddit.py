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
    param=[]
    if request.method == 'GET':
        for i in subreddits:
            if request.args.get(i) != None:
                param.append(i)
                reddit_url = requests.get(url+f"/r/{i}/top/?t=month",headers=headers)
                content = BeautifulSoup(reddit_url.text,"html.parser")
                div = content.find("div","rpBJOHq2PR60pnwJlUyP0")
                for item in div:
                    if item.find("a",{"data-click-id":"body"}):
                        vote = item.find("div","_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo").text
                        if "k" in vote:
                            vote = float(vote.replace("k","")) * 1000
                        else:
                            items.append({
                                'url'   : item.find("a",{"data-click-id":"body"}).attrs['href'],
                                'title' : item.find("a",{"data-click-id":"body"}).text,
                                'vote'  : float(vote),
                                'lang'  : i
                            })
                    else:
                        pass
        items.sort(key=lambda x: x['vote'],reverse=True)         
        print(items)    
    return render_template("read.html",items=items,param=param)


app.run()