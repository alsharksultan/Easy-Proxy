# coding=utf-8
#!/usr/bin/python
import requests,os,sys, subprocess, requests, time, platform

#Détection de l'OS
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
   
   

booom = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
 """
 
banner = """
 ▄▄▄·▄▄▄        ▐▄• ▄  ▄· ▄▌.▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄·▄▄▄ .
▐█ ▄█▀▄ █·▪      █▌█▌▪▐█▪██▌▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄█▀▄.▀·
 ██▀·▐▀▀▄  ▄█▀▄  ·██· ▐█▌▐█▪▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀·▐▀▀▪▄
▐█▪·•▐█•█▌▐█▌.▐▌▪▐█·█▌ ▐█▀·.▐█▄▪▐█▐███▌▐█•█▌▐█ ▪▐▌▐█▪·•▐█▄▄▌
.▀   .▀  ▀ ▀█▄▀▪•▀▀ ▀▀  ▀ •  ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀    ▀▀▀ 					  
"""
 
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
print(bcolors.WARNING + booom + bcolors.ENDC)    
print(bcolors.OKBLUE + bcolors.UNDERLINE + "Tu as choisis le module generation proxy" + bcolors.ENDC)
time.sleep(1)
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
proxy_number = 0
print(bcolors.HEADER + banner + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules ProxyScrape" + bcolors.ENDC)
print(" ")

#Choix du type de proxy
proxy_type = int(input("Proxy Type  ?\n\n[1] SOCKS4\n[2] SOCKS5\n[3] HTTP\n[4] TOUS \n\n[>] "))
if proxy_type == 1:
    proxy_type = "socks4"
elif proxy_type == 2:
    proxy_type = "socks5"
elif proxy_type == 3:
    proxy_type = "http"
elif proxy_type == 4:
    proxy_type = "all"
else:
    clear()
    print(bcolors.HEADER + banner + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
    print(" ")
    sys.exit("Votre choix est incorrect.")


clear()
print(bcolors.HEADER + banner + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
print(" ")
print("Type de proxy: " + proxy_type+"\n\n")

#Choix du timeout
try:
    proxy_timeout = int(input("Timeout  ?\n\n[>] "))
except:
    clear()
    print(bcolors.HEADER + banner + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
    print(" ")
    sys.exit("Votre choix est incorrect.")

clear()
print(bcolors.HEADER + banner + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
print(" ")
print("Type de proxy: " + proxy_type)
print("Timeout : " + str(proxy_timeout)+"\n\n")

#Choix de l'anonymat du proxy
proxy_anon = int(input("Proxy Anonimity  ?\n\n[1] ELITE\n[2] ANONYMOUS\n[3] TRANSPARENT\n[4] TOUS \n\n[>] "))
if proxy_anon == 1:
    proxy_anon = "elite"
elif proxy_anon == 2:
    proxy_anon = "anonymous"
elif proxy_anon == 3:
    proxy_anon = "transparent"
elif proxy_anon == 4:
    proxy_anon = "all"
else:
    clear()
    print(bcolors.HEADER + banner + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
    print(" ")
    sys.exit("Votre choix est incorrect.")

clear()
print(bcolors.HEADER + banner + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
print(" ")
print("Type de proxy: " + proxy_type)
print("Timeout : " + str(proxy_timeout))
print("Proxy Anonimity : " + proxy_anon+"\n\n")

#URL de l'API avec les choix de l'user
req = "https://api.proxyscrape.com/?request=displayproxies&proxytype="+proxy_type+"&timeout="+str(proxy_timeout)+"&anonymity="+proxy_anon+"&ssl=yes"
#GET l'url
r = requests.get(req)
#Obtenir la liste de tous les proxys
proxies = r.text.split("\n")
#Ouvrir le fichier proxys.txt
file = open("proxys.txt","a")

#Pour chaque proxy
for prox in proxies:
    proxy_number+=1 #+1 proxy 
    file.write(prox) #enregistrer le proxy
file.close() #fermer le fichier
clear()
print(bcolors.HEADER + banner + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.UNDERLINE + "$ Modules Anti Public" + bcolors.ENDC)
print(" ")
print(bcolors.OKGREEN + "[+] Terminé !\n" + bcolors.ENDC + bcolors.UNDERLINE + "Nombre de proxys trouvés :" + bcolors.ENDC + " " +str(proxy_number))
input("Appuie sur entrer pour continuer...")
