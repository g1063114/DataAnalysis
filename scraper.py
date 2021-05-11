from flask import Flask, render_template, request
import requests

base_url = "http://hn.algolia.com/api/v1"

new = f"{base_url}/search_by_date?tags=story"

popular = f"{base_url}/search?tags=story"

db = {}

app = Flask("Scrapper")

@app.route("/",methods=['GET'])
def home():
    order = request.args.get('order_by')
    if order == None or order == "popular":
        url = popular
        from_db = db.get(order)
        if from_db:
            items = from_db
        else:
            items = requests.get(url).json()
            db[order] = items
    else:
        url = new
        from_db = db.get(order)
        if from_db:
            items = from_db
        else:
            items = requests.get(url).json()
            db[order] = items

    #print(items.get('hits'))
    print(db)

    return render_template("home.html",items=items.get('hits'))

@app.route("/<id>")
def detail(id):
    page_url = base_url + f"/items/{id}"
    




app.run()