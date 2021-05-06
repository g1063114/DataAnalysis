import os
import requests

def split_urls(urls):
    url_list = urls.split(",")
    for i in range(len(url_list)):
        url_list[i] = url_list[i].strip().lower()
        if "http://" in url_list[i]:
            pass
        else:
            url_list[i] = "http://" + url_list[i]

        if ".com" in url_list[i]:
            pass
        else:
            print(url_list[i] + "is not a valid URL")
            return 0
    return url_list

def is_running(list):
    for i in range(len(list)):
        check = requests.get(list[i])

        if check.status_code == 200:
            print(list[i] + " is Up!")
        elif check.status_code == 404:
            print(list[i] + " is Down!")


while True:
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma)")
    urls = input()
    url_list = split_urls(urls)
    if url_list != 0:
        is_running(url_list)

    print("Do you want to start over? y/n")
    answer = input()
    if answer == 'y':
        os.system('cls')
        pass
    elif answer == 'n':
        print("k.bye!")
        break
    else:
        print("That's not a valid answer")
