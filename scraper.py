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

    #print(db)

    return render_template("home.html",items=items.get('hits'),baseurl=base_url)

@app.route("/<id>")
def detail(id):
    page_url = base_url + f"/items/{id}"
    items = requests.get(page_url).json()
    comment = items.get('children')
    db[id] = items

    print(comment)
    return render_template("detail.html",items=items,comment=comment)
    




app.run()