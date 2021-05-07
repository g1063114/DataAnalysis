import requests
from bs4 import BeautifulSoup

def get_code():
    urls = requests.get("https://www.iban.com/currency-codes")
    content = BeautifulSoup(urls.text,"html.parser")
    tb_list = content.find("tbody")
    tr_list = tb_list.find_all("tr")
    country_list = []
    for tr in tr_list:
        td_list = tr.find_all("td")
        if td_list[1].string.find("universal") == -1:
            country_list.append({
                'number'      : int(td_list[3].string),
                'country'   : td_list[0].string,
                'code'      : td_list[2].string
            })
        else:
            pass
    country_list.sort(key=lambda x: x['number'])
    return country_list

def print_list(clist):
    for i in clist:
        print("# " + str(i.get('number')) + " " + i.get('country'))
    
def main():
    print("Hello! Please choose select a country by number: ")
    country_list = get_code()
    print_list(country_list)
    while True:
        try:
            num = int(input("#: "))
            if num > 1000:
                print("choose a number from the list")
            else:
                for i in country_list:
                    if num == i.get('number'):
                        print("You chose " + i.get('country'))
                        print("The currency code is " + i.get('code'))
                        break
        except:
            print("That wasn't a number")
    
main()