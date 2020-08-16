#This script is made by Hacker wasi 
#Don't copy this source code with out cradit.
#MIT License
#Copyright (c) 2020 Evil Devil
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os, datetime
import requests, json
from core.bssidFinder import bssidFinder
from core.employee_lookup import employee_lookup
from core.google import google
from core.hashDecrypt import hashdecrypt
from core.ipFinder import ipFinder
from core.mailToIP import mailToIP
from core.profilerFunc import profilerFunc
from core.searchAdresse import searchAdresse
from core.searchTwitter import searchTwitter
from core.searchPersonne import searchPersonne
from core.searchInstagram import searchInstagram
from core.searchUserName import searchUserName
from core.searchNumber import searchNumber
from core.searchEmail import SearchEmail
from core.Profiler import Profiler
from core.facebookStalk import facebookStalk

def init():
    global version
    global monip, monpays, codemonpays, pathDatabase
    global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
    global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
    global Profiler

    version = '6.0.2'

    pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
    pathDatabase = "\\".join(pathDatabase)+"\\Watched"

    monip = requests.get("https://api.ipify.org/").text

    monpays = requests.get("http://ip-api.com/json/"+monip).text
    value = json.loads(monpays)
    monpays = value['country']
    codemonpays = value['countryCode']

    if not os.path.exists(pathDatabase):
        os.mkdir(pathDatabase)
