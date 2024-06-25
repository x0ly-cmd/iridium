# ABSEN TALENTA WITH TIME SETTING
# Author    : @raihante
# Date      : 15/03/24

import os
import requests
import schedule
import time
import datetime
import json

def banner():
    os.system('cls')
    print('=========================================')
    print('')
    print('\033[1;92m    ____  ____  ____  __  ________   ________\033[1;m')
    print('\033[1;92m   / __ \/ __ \/ __ \/  |/  /  _/ | / /_  __/\033[1;m')
    print('\033[1;92m  / / / / / / / /_/ / /|_/ // //  |/ / / /   \033[1;m')
    print('\033[1;92m / /_/ / /_/ / _, _/ /  / // // /|  / / /    \033[1;m')
    print('\033[1;92m/_____/\____/_/ |_/_/  /_/___/_/ |_/ /_/     \033[1;m')
    print('\033[1;91m # [C] \033[1;93mHan\033[1;m\033[1;m                 \033[1;92m[AUTO-CLAIM] $$ \033[1;m')
    print('')
    print('=========================================')
    print('\033[1;92mWelcome & Enjoy !\033[1;m')
    print('\033[1;93mHaving Troubles? PM Discord [x0ly]\033[1;m')

def Convert(string): 
    li = list(string.split('"')) 
    return li 

def runforeva(): 
    value = True
    while (value):
        postrequest()

def postrequest():
    tanggal = datetime.datetime.now().strftime("%Y-%m-%d")
    urlstatus = 'https://api.dormint.io/tg/farming/status'
    urlstart = 'https://api.dormint.io/tg/farming/start'
    urlclaim = 'https://api.dormint.io/tg/farming/claimed'

    head = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
    }

    textpayload = '{"auth_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk0NTY0MTIsInRnX2lkIjo3NjgwMTQ2MzZ9.cqUzKQcSvjFsccZhCuKswQjAhucehIj3c15HaXtwCII"}'



    #print(rsplit[12].strip(':,'))
    try:
        r = requests.post(urlstatus,headers=head,data=textpayload)
        rsplit = Convert(r.text)
        #print(rsplit)
        print("")
        print('\033[1;93m[INFO] Balance :', rsplit[14].strip(':,'), '\033[1;m')
    except:
        print('\033[1;91m[ERROR] Restarting!!\033[1;m')
        time.sleep(5)
        runforeva()

    try:
        r2 = requests.post(urlstart,headers=head,data=textpayload)
        print('\033[1;96m[INFO] Farming Started!\033[1;m')
    except:
        print('\033[1;91m[ERROR] Restarting!!\033[1;m')
        time.sleep(5)
        runforeva()

    try:
        r3 = requests.post(urlclaim,headers=head,data=textpayload)
        print('\033[1;92m[INFO] Claimed!\033[1;m')
    except:
        print('\033[1;91m[ERROR] Restarting!!\033[1;m')
        time.sleep(5)
        runforeva()


# NYALAIN SENDIRI ABANGKUHH
banner()
runforeva()

