import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

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

def ask(clist, num):
    try:
        if num >= 1000:
            print("choose a number from the list")
        else:
            for i in clist:
                    if num == i.get('number'):
                        print(i.get('country')+'\n')
                        code = i.get('code')
    except:
            print("That wasn't a number")
    return code

def exchange(num1, num2, amount):
    urls = requests.get(f"https://wise.com/gb/currency-converter/{num1}-to-{num2}-rate?amount={amount}")
    content = BeautifulSoup(urls.text,"html.parser")
    from_num = content.find("input",{'id':'cc-amount-from'}).get('value')
    to_num = float(content.find("input",{'id':'rate'}).get('value')) * float(from_num)
    print(format_currency(from_num, num1,locale="ko_KR") + " is " + format_currency(to_num, num2,locale="ko_KR"))
    

def main():
    print("Hello! Please choose select a country by number: ")
    country_list = get_code()
    print_list(country_list)
  
    print("Where are you from? Choose a country by number.")
    temp = int(input("#: "))
    num1 = ask(country_list, temp)
    print("Now choose another country.")
    temp2 = int(input("#: "))
    num2 = ask(country_list, temp2)
    print(f"How many {num1} do you want to convert to {num2}?")
    while True:
        try:
            amount = int(input("#: "))
            exchange(num1,num2,amount)
            break
        except:
            print("That wasn't a number")
        
main()