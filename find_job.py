
from warnings import resetwarnings
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, send_file
import csv

wework_url = "https://weworkremotely.com/remote-jobs/search?"
remote_url = "https://remoteok.io/"
stack_url = "https://stackoverflow.com/jobs?r=true"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

db = {}

def wework(key):
    items = []
    if db.get(key):
        items = db
    else:
        url = wework_url + "term=" + key
        get_url = requests.get(url)
        content = BeautifulSoup(get_url.text,"html.parser")
        div = content.find_all("li","feature")
        for i in div:
            aref = i.find_all("a")[1]
            items.append({
                'url'       : "https://weworkremotely.com/" + aref.attrs['href'],
                'title'     : i.find("span","title").text,
                'company'   : i.find("span","company").text
            })
        db[key] = items
        remote(items,key)
        stack(items,key)
    return items

def remote(temp,key):
    url = remote_url + "remote-" + key + "-jobs"
    get_url = requests.get(url,headers=headers)
    content = BeautifulSoup(get_url.text,"html.parser")
    table = content.find("table",{"id":"jobsboard"})
    tbody = table.find_all("tr","job")
    for i in tbody:
        i.find("td","company position company_and_position")
        temp.append({
            'url'       : "https://remoteok.io/" + i.find("a").attrs['href'],
            'title'     : i.find("h2",{"itemprop":"title"}).text,
            'company'   : i.find("h3",{"itemprop":"name"}).text
        })
    db[key] = temp


def stack(temp,key):
    url = stack_url + "&q=" + key
    get_url = requests.get(url)
    content = BeautifulSoup(get_url.text,"html.parser")
    div = content.find_all("div","grid--cell fl1")
    for i in div:
        temp.append({
            'url'       : "https://stackoverflow.com" + i.find("a").attrs['href'],
            'title'     : i.find("a").text,
            'company'   : i.find("span").text
        })
    db[key] = temp

def save_to_file(items,key):
    file = open("jobs.csv", mode="w",encoding='utf8')
    writer = csv.writer(file)
    writer.writerow(["url","title","company"])
    for item in items:
        write_list = [item.get('url'),item.get('title'),item.get('company')]
        writer.writerow(write_list)
 


app = Flask("job")

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/list", methods=['POST','GET'])
def content():
    res=[]
    if request.method == 'GET':
        term = request.args.get('term')
        term = term.lower()
        res = wework(term)
        items = db.get(term)
        print(items)
    return render_template("list.html",items=items,length=len(items),term=term)

@app.route("/export")
def export():
    try:
        term = request.args.get('term')
        print(term)
        if not term:
            raise Exception()
        jobs = db.get(term)
        print(jobs)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run()