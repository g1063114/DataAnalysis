import requests
from bs4 import BeautifulSoup
import csv

def scrape_site():
    url = requests.get("http://www.alba.co.kr/")
    content = BeautifulSoup(url.text,"html.parser")
    div = content.find("div",{"id":"MainSuperBrand"})
    items = div.find("ul","goodsBox")
    item_list = items.find_all("li")
    company_list = []
    for company in item_list:
        if company.find("span","company") == None:
            pass
        else:
            company_list.append({
                'company' : company.find("span","company").string,
                'url' : company.find("a","goodsBox-info").get('href')
            })
    return company_list

def request_company(clist):
    for company in clist:
        send = requests.get(company.get('url'))
        content = BeautifulSoup(send.text,"html.parser")
        tbody = content.find("tbody")
        data_list = []
        count = 1
        for i in tbody.find_all("tr"):
            if count%2 == 1:
                tds = i.find_all("td")
                if len(tds) < 2:
                    break
                else:
                    data_list.append({
                        'place' : tds[0].text,
                        'title' : company.get('company'),
                        'time'  : tds[2].find("span").text,
                        'pay'   : tds[3].text,
                        'date'  : tds[4].text
                    })
                count = count+1
            else:
                count = count+1
                pass
            print(data_list)
        save_to_file(company.get('company'),data_list)    
        

def save_to_file(cname, dlist):
    file = open(cname, mode="w",encoding='utf8')
    writer = csv.writer(file)
    writer.writerow(["place","title","time","pay","date"])
    for item in dlist:
        write_list = [item.get('place').replace("\xa0"," "),item.get('title'),item.get('pay'),item.get('date')]
        print(write_list)
        writer.writerow(write_list)

def main():
    company_list = scrape_site()
    data_list = request_company(company_list)

main()