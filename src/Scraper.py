import requests
import json 

def fetch_rooms(HTB_TOKEN,source_url,userId):
    if "tryhackme.com" in source_url:
        return thm(source_url,userId)
    elif "hackthebox.com" in source_url:
        return htb(HTB_TOKEN,source_url,userId)

def thm(source_url,userId):
    json_file = ""
    rooms = []
    offset=1
    while json_file != []:
        url_thm = source_url+userId+"&limit=10&page="+str(offset)
        page = requests.get(url_thm)
        json_file = json.loads(page.content)
        for room in json_file:
            if room["type"]=="challenge":
                rooms.append({"title": room["title"], "url": "https://tryhackme.com/room/"+room["code"], "id": room['code']})
        offset+=1
    return rooms

def htb(HTB_TOKEN,source_url,userId):
    headers = {
        'Authorization':  'Bearer '+HTB_TOKEN,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    url_htb = "https://www.hackthebox.com/api/v4/user/profile/activity/"+userId
    page = requests.get(url_htb, headers=headers)
    json_file = json.loads(page.content)['profile']['activity']
    rooms = []
    for room in json_file:
        if room['object_type']=="machine":
            rooms.append({"title": room["name"]+" - "+room["type"], "url": "https://app.hackthebox.com/machines/"+str(room["id"]), "id": room["id"]})
    return rooms