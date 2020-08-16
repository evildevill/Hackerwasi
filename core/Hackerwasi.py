# -*- coding: utf-8 -*-

__version__ = 6.0

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style

init()
warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Veuillez lancer la version 3 de python.")

checkVersion()

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def loadlib():

	import requests, json

	import datetime

	# fonction
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

	global monip, monpays, codemonpays, pathDatabase
	global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
	global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
	global Profiler


	monip = requests.get("https://api.ipify.org/").text

	monpays = requests.get("http://ip-api.com/json/"+monip).text
	value = json.loads(monpays)
	monpays = value['country']
	codemonpays = value['countryCode']

	pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
	pathDatabase = "\\".join(pathDatabase)+"\\Watched"

	if not os.path.exists(pathDatabase):
		os.mkdir(pathDatabase)

def loadingHack(importlib):
	chaine = "[*]"+' Start HackErWaSi...'
	charspec = "$*.X^%_/\\#~!?;"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
			if len(chainehack+r) <= len(chaine):
				pass
			else:
				r = ""
			sys.stdout.write('\r'+chainehack+r)
			time.sleep(0.06)

def loadingUpper(importlib):

	string = "Start HackErWaSi"
	string = list(string)
	nb = len(string)

	while importlib.is_alive():
		x = 0
		while x < nb:
			c = string[x]
			c = c.upper()
			string[x] = c
			sys.stdout.write("\r[*] "+''.join(string) +'...')
			time.sleep(0.1)
			c = string[x]
			c = c.lower()
			string[x] = c
			x += 1

def loadingTextPrint(importlib):
	string = "Start HackErWaSi"

	while importlib.is_alive():

		space = " " * 100
		sys.stdout.write("\r"+space)
		
		x = 1

		while x <= len(string):
			times = "0."
			times += str(random.choice(range(1, 3)))
			sys.stdout.write("\rroot@HackErWaSi:~$ "+string[:x]+"|")
			time.sleep(float(times))
			x += 1

def thread_loading():

	num = random.choice([1, 2, 3])

	importlib = threading.Thread(target=loadlib)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))
	elif num == 2:
		load = threading.Thread(target=loadingUpper(importlib))
	elif num == 3:
		load = threading.Thread(target=loadingTextPrint(importlib))

	load.start()
	importlib.join()
	load.join()

thread_loading()

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)


from datetime import date
today_date = date.today()

header1 = """
   ___ ___                __                                       .__ 
 /   |   \_____    ____ |  | __ _____________  _  _______    _____|__|
/    ~    \__  \ _/ ___\|  |/ // __ \_  __ \ \/ \/ /\__  \  /  ___/  |
\    Y    // __ \\  \___|    <\  ___/|  | \/\     /  / __ \_\___ \|  |
 \___|_  /(____  /\___  >__|_ \\___  >__|    \/\_/  (____  /____  >__|
       \/      \/     \/     \/    \/                    \/     \/      
"""

header2 = """

      ___           ___           ___           ___           ___           ___           ___           ___           ___                 
     /\__\         /\  \         /\  \         /\__\         /\  \         /\  \         /\__\         /\  \         /\  \          ___   
    /:/  /        /::\  \       /::\  \       /:/  /        /::\  \       /::\  \       /:/ _/_       /::\  \       /::\  \        /\  \  
   /:/__/        /:/\:\  \     /:/\:\  \     /:/__/        /:/\:\  \     /:/\:\  \     /:/ /\__\     /:/\:\  \     /:/\ \  \       \:\  \ 
  /::\  \ ___   /::\~\:\  \   /:/  \:\  \   /::\__\____   /::\~\:\  \   /::\~\:\  \   /:/ /:/ _/_   /::\~\:\  \   _\:\~\ \  \      /::\__\
 /:/\:\  /\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:::::\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/_/:/ /\__\ /:/\:\ \:\__\ /\ \:\ \ \__\  __/:/\/__/
 \/__\:\/:/  / \/__\:\/:/  / \:\  \  \/__/ \/_|:|~~|~    \:\~\:\ \/__/ \/_|::\/:/  / \:\/:/ /:/  / \/__\:\/:/  / \:\ \:\ \/__/ /\/:/  /   
      \::/  /       \::/  /   \:\  \          |:|  |      \:\ \:\__\      |:|::/  /   \::/_/:/  /       \::/  /   \:\ \:\__\   \::/__/    
      /:/  /        /:/  /     \:\  \         |:|  |       \:\ \/__/      |:|\/__/     \:\/:/  /        /:/  /     \:\/:/  /    \:\__\    
     /:/  /        /:/  /       \:\__\        |:|  |        \:\__\        |:|  |        \::/  /        /:/  /       \::/  /      \/__/    
     \/__/         \/__/         \/__/         \|__|         \/__/         \|__|         \/__/         \/__/         \/__/                
"""

header5 = """
      ___           ___           ___           ___           ___           ___           ___           ___           ___                 
     /__/\         /  /\         /  /\         /__/|         /  /\         /  /\         /__/\         /  /\         /  /\        ___     
     \  \:\       /  /::\       /  /:/        |  |:|        /  /:/_       /  /::\       _\_ \:\       /  /::\       /  /:/_      /  /\    
      \__\:\     /  /:/\:\     /  /:/         |  |:|       /  /:/ /\     /  /:/\:\     /__/\ \:\     /  /:/\:\     /  /:/ /\    /  /:/    
  ___ /  /::\   /  /:/~/::\   /  /:/  ___   __|  |:|      /  /:/ /:/_   /  /:/~/:/    _\_ \:\ \:\   /  /:/~/::\   /  /:/ /::\  /__/::\    
 /__/\  /:/\:\ /__/:/ /:/\:\ /__/:/  /  /\ /__/\_|:|____ /__/:/ /:/ /\ /__/:/ /:/___ /__/\ \:\ \:\ /__/:/ /:/\:\ /__/:/ /:/\:\ \__\/\:\__ 
 \  \:\/:/__\/ \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:::::/ \  \:\/:/ /:/ \  \:\/:::::/ \  \:\ \:\/:/ \  \:\/:/__\/ \  \:\/:/~/:/    \  \:\/\
  \  \::/       \  \::/       \  \:\  /:/   \  \::/~~~~   \  \::/ /:/   \  \::/~~~~   \  \:\ \::/   \  \::/       \  \::/ /:/      \__\::/
   \  \:\        \  \:\        \  \:\/:/     \  \:\        \  \:\/:/     \  \:\        \  \:\/:/     \  \:\        \__\/ /:/       /__/:/ 
    \  \:\        \  \:\        \  \::/       \  \:\        \  \::/       \  \:\        \  \::/       \  \:\         /__/:/        \__\/  
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/                
"""

header6 = """
 _   _            _                               _ 
| | | | __ _  ___| | _____ _ ____      ____ _ ___(_)
| |_| |/ _` |/ __| |/ / _ \ '__\ \ /\ / / _` / __| |
|  _  | (_| | (__|   <  __/ |   \ V  V / (_| \__ \ |
|_| |_|\__,_|\___|_|\_\___|_|    \_/\_/ \__,_|___/_|
"""

header7 = """
   __ __         __                           _ 
  / // /__ _____/ /_____ _____    _____ ____ (_)
 / _  / _ `/ __/  '_/ -_) __/ |/|/ / _ `(_-</ / 
/_//_/\_,_/\__/_/\_\\__/_/  |__,__/\_,_/___/_/                                                        
"""

header8 = """
         _                                                                                
          ' )     )                    /'  _/                                               
          /'    /'                   /' _/~                                                 
       ,/'    /' ____     ____    ,/'_/~  ____      ____   .   . ,   ,   ____     ____     O
      /`---,/' /'    )  /'    )--/\/~   /'    )   )'    )--|   |/   /  /'    )  /'    )--/' 
    /'    /' /'    /' /'       /'  \  /(___,/'  /'         |  /|  /' /'    /'  '---,   /'   
(,/'     (_,(___,/(__(___,/  /'     \(________/'          _|/' |/(__(___,/(__(___,/   (__                                                                                                                  
"""

header9 = """
    ___    _____  _______    __     _    _        __     ___    ____    _____  ______       ___      __
\  |   |  /    /  \     /  __) \   | )  / \    ___) |    \  |  |    |  |    /  \     )  ____) (_    _) 
 |  \_/  |    /    \   |  /     |  |/  /   |  (__   |     ) |  |    |  |   /    \   (  (___     |  |   
 |   _   |   /  ()  \  | |      |     (    |   __)  |    /  |  |    |  |  /  ()  \   \___  \    |  |   
 |  / \  |  |   __   | |  \__   |  |\  \   |  (___  | |\ \   \  \/\/  /  |   __   |  ____)  )  _|  |_  
/  |___|  \_|  (__)  |__\    )_/   |_)  \_/       )_| |_\ \___\      /___|  (__)  |_(      (__(      )_                                                             
"""

header11 = """
.-..-.             .-.                                     _ 
: :; :             : :.-.                                 :_;
:    : .--.   .--. : `'.' .--. .--. .-..-..-. .--.   .--. .-.
: :: :' .; ; '  ..': . `.' '_.': ..': `; `; :' .; ; `._-.': :
:_;:_;`.__,_;`.__.':_;:_;`.__.':_;  `.__.__.'`.__,_;`.__.':_;   
"""

header12 = """                                             
          _______  _______  _        _______  _______           _______  _______ _________
|\     /|(  ___  )(  ____ \| \    /\(  ____ \(  ____ )|\     /|(  ___  )(  ____ \\__   __/
| )   ( || (   ) || (    \/|  \  / /| (    \/| (    )|| )   ( || (   ) || (    \/   ) (   
| (___) || (___) || |      |  (_/ / | (__    | (____)|| | _ | || (___) || (_____    | |   
|  ___  ||  ___  || |      |   _ (  |  __)   |     __)| |( )| ||  ___  |(_____  )   | |   
| (   ) || (   ) || |      |  ( \ \ | (      | (\ (   | || || || (   ) |      ) |   | |   
| )   ( || )   ( || (____/\|  /  \ \| (____/\| ) \ \__| () () || )   ( |/\____) |___) (___
|/     \||/     \|(_______/|_/    \/(_______/|/   \__/(_______)|/     \|\_______)\_______/
                 \\\\
                  \\\\_   \\\\
                   (')   \\\\_
 HackErWaSi -> / )=.---(') <- Privacy
                o( )o( )_-\_
"""

header13 = """
 _           _                            _                                                                                    _          
(_)         (_)                          (_)                                                                                  (_)         
(_)         (_)   _  _  _        _  _  _ (_)     _  _  _  _  _   _       _  _  _             _   _  _  _       _  _  _  _   _  _          
(_) _  _  _ (_)  (_)(_)(_) _   _(_)(_)(_)(_)   _(_)(_)(_)(_)(_)_(_)_  _ (_)(_)(_)           (_) (_)(_)(_) _  _(_)(_)(_)(_) (_)(_)         
(_)(_)(_)(_)(_)   _  _  _ (_) (_)        (_) _(_) (_) _  _  _ (_) (_)(_)      (_)     _     (_)  _  _  _ (_)(_)_  _  _  _     (_)         
(_)         (_) _(_)(_)(_)(_) (_)        (_)(_)_  (_)(_)(_)(_)(_) (_)         (_)_  _(_)_  _(_)_(_)(_)(_)(_)  (_)(_)(_)(_)_   (_)         
(_)         (_)(_)_  _  _ (_)_(_)_  _  _ (_)  (_)_(_)_  _  _  _   (_)           (_)(_) (_)(_) (_)_  _  _ (_)_  _  _  _  _(_)_ (_) _       
(_)         (_)  (_)(_)(_)  (_) (_)(_)(_)(_)    (_) (_)(_)(_)(_)  (_)             (_)   (_)     (_)(_)(_)  (_)(_)(_)(_)(_) (_)(_)(_)   
"""

header14 = """
 _   _            _                               _ 
| | | |          | |                             (_)
| |_| | __ _  ___| | _____ _ ____      ____ _ ___ _ 
|  _  |/ _` |/ __| |/ / _ \ '__\ \ /\ / / _` / __| |
| | | | (_| | (__|   <  __/ |   \ V  V / (_| \__ \ |
\_| |_/\__,_|\___|_|\_\___|_|    \_/\_/ \__,_|___/_|
"""

header15 = """                                                                                             
 __ __   ____    __  __  _    ___  ____  __    __   ____  _____ ____ 
|  T  T /    T  /  ]|  l/ ]  /  _]|    \|  T__T  T /    T/ ___/l    j
|  l  |Y  o  | /  / |  ' /  /  [_ |  D  )  |  |  |Y  o  (   \_  |  T 
|  _  ||     |/  /  |    \ Y    _]|    /|  |  |  ||     |\__  T |  | 
|  |  ||  _  /   \_ |     Y|   [_ |    \l  `  '  !|  _  |/  \ | |  | 
|  |  ||  |  \     ||  .  ||     T|  .  Y\      / |  |  |\    | j  l 
l__j__jl__j__j\____jl__j\_jl_____jl__j\_j \_/\_/  l__j__j \___j|____j                                                                                                                                                               
"""

header16 = """
 _______              __                                     __ 
|   |   |.---.-.----.|  |--.-----.----.--.--.--.---.-.-----.|__|
|       ||  _  |  __||    <|  -__|   _|  |  |  |  _  |__ --||  |
|___|___||___._|____||__|__|_____|__| |________|___._|_____||__|               
"""

header17 = """
 ____ ____ ____ ____ ____ ____      
||E |||V |||I |||L |||H |||A ||     
||__|||__|||__|||__|||__|||__||     
|/__\|/__\|/__\|/__\|/__\|/__\|     
 ____ ____ ____ ____ ____ ____ ____ 
||C |||K |||E |||R |||W |||A |||SI||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
"""

header18 = """
                                                              
                                                  ..                                                                .x+=:.      .    
         .xHL                               < .z@8"`                                x=~                            z`    ^%    @88>  
      .-`8888hxxx~                           !@88E                      .u    .    88x.   .e.   .e.                   .   <k   %8P   
   .H8X  `%888*"            u           .    '888E   u         .u     .d88B :@8c  '8888X.x888:.x888        u        .@8Ned8"    .    
   888X     ..x..        us888u.   .udR88N    888E u@8NL    ud8888.  ="8888f8888r  `8888  888X '888k    us888u.   .@^%8888"   .@88u  
  '8888k .x8888888x   .@88 "8888" <888'888k   888E`"88*"  :888'8888.   4888>'88"    X888  888X  888X .@88 "8888" x88:  `)8b. ''888E` 
   ?8888X    "88888X  9888  9888  9888 'Y"    888E .dN.   d888 '88%"   4888> '      X888  888X  888X 9888  9888  8888N=*8888   888E  
    ?8888X    '88888> 9888  9888  9888        888E~8888   8888.+"      4888>        X888  888X  888X 9888  9888   %8"    R88   888E  
 H8H %8888     `8888> 9888  9888  9888        888E '888&  8888L       .d888L .+    .X888  888X. 888~ 9888  9888    @8Wou 9%    888E  
'888> 888"      8888  9888  9888  ?8888u../   888E  9888. '8888c. .+  ^"8888*"     `%88%``"*888Y"    9888  9888  .888888P`     888&  
 "8` .8" ..     88*   "888*""888"  "8888P'  '"888*" 4888"  "88888%       "Y"         `~     `"       "888*""888" `   ^"F       R888" 
    `  x8888h. d*"     ^Y"   ^Y'     "P'       ""    ""      "YP'                                     ^Y"   ^Y'                 ""   
      !""*888%~                                                                                                                      
      !   `"  .                                                                                                                      
      '-....:~
"""

def lb_header():

    headers = [header1, header2, header5, header6, header7, header8, header9,
        header11, header12, header13, header14, header15, header16, header17, header18]
    return(random.choice(headers))

helpMain = """
 Name                       Action
 ----                       ------<
 Lookup                     Do some research on a person.
 Other Tool                 Use tools other than recognition.
 Make file                  Create a '.txt' file to write the information obtained.
 Show Database              Access the database.

 Exit                       Exit the software.
 Help                       Affiche se message.
 Clear                      Clear the screen."""

helpLookup = """
 Name                             Action
 ----                             ------
[1]  Personne lookup                  Do research with a name, first name and (city).
[2]  Username lookup                  Do research with a pseudonym.
[3]  Adresse lookup                   Search with an address.
[4]  Phone lookup                     Do research with a phone number.
[5]  IP lookup                        Searching with an IP address.
[6]  SSID locator                     Searching with a MAC / BSSID address
[7]  Email lookup                     Do research with an email address.
[8]  Mail tracer                      Do research with the header of an email.
[9]  Employés recherche               Finds the employees of a company.
[10] Google search                    Do research on google.
[11] Facebook graphSearch             Do research using graphSearch.
[12] twitter info                     Retrieve information from a Twitter account.
[13] instagram info                   Retrieve information from a Instagram account.

[b]  Back main menu                   Return to the main menu.
[e]  Exit script                      To exit the software.
[c]  Clear screen                     Clear the screen.
[h]  Help Message                     Display this message."""
helpOtherTool = """
 Name                             Action
 ----                             ------
 Hash decrypter                   Try to decrypt a hash via an online database.

 Back main menu                   Return to the main menu.
 Exit script                      To exit the software.
 Clear screen                     Clear the screen."""

helpProfiler = """
 Name                      Action
 ----                      ------
 Search Profiles           Search for a profile in the database.
 Show all Profiles         Displays all the profiles in the database.

 Exit Database             Exit the database to return to the main menu.
 Help message              Message displays
"""

helpCountry = """
 Name                      Action
 ----                      ------
 FR                        Use French services.
 BE                        Use Belgian services.
 CH                        Use Swiss services.
 LU                        Use Luxembourgish services.
 All                       Use all services.

 Back main menu            Return to the main menu.
 Exit script               To exit the software.
 Clear screen              Clear the screen."""

mainOption = """
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Change country

 [e] Exit script    [h] Help Message    [c] Clear Screen"""

text = ['Press F to hack', 'LEAVE ME HERE', 'The security is an illusion.', 'Profiler ctOS v2.0', 'DedSec takeover', 'Fsociety00.dat', 'Evil Corp',
 'Hello, friend', 'Hacking is our weapon', 'Hello, World', 'Login the world...', 'Big Brother is watching you.', 'Fuck Society', 'Wrench is calling...',
 'The control is an illusion.', 'install google_crack.exe...', 'you are free ! lol no, it was a joke.', 'you are a 1 or a 0 ?', 'Matraque: 1 - Genou: 0', 'Je veux que tu comprenne... Que tu ne sera plus jamais libre..', 'Tu pense être intouchable... Je vais briser tes illusion...',
 'je veux que tu sache... que tu n\'es plus anonyme...', 'Snapchat: T-Bone sent you a new message.', 'LulzSec <3 <3', '<3 Kraken Security OS is bae <3', 'DedSec is now in LinkedIn !',
 'FRANCE World champion 2018 !!', '~~(8:> is Defalt ~~(8:>', 'Facebook: Neo in a relationship with Elliot Alderson.', 'Just.. fuck the society.', 'locating 127.0.0.1 ... No match found', 
 '101100100101100 01100110010110011001', '101100 0110011001', 'c2V5cHRvbyBteSBsb3Zl', '1 item in your web hisotry: \'Fkk cuckold how to make your wife a hotwife zootube\'', '49 20 4c 4f 56 45 20 55', 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6VUS3OKVZGQYSLJQ3GO===', 'Regarde derrière toi...',
 'dW4gZCdldXggdHJvdWUgw6AgcXUnYSB0J3JlIHNlaW4gcXVlIHNpIGNlIGNldHRl', 'Send me nudes: hackerwasi1@gmail,com', "Access point 'AP-Zone51' was found nearby."]

lookupOption = """
 [1] Personne lookup          [8] Mail tracer                     
 [2] Username lookup          [9] Employés recherche
 [3] Adresse lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearch          
 [5] IP lookup                [12] twitter info
 [6] SSID locator             [13] instagram info
 [7] Email lookup             

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen"""

otherToolOption = """
 [1] Hash decrypter

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen 
"""

profilerOption = """
 [1] Profiler
 [2] Show all Profiles   
 [3] Create profile

 [b] back main menu    [c] Clear screen   [h] Help message
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg) 
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)

 [e] back main menu   [c] Clear screen   [h] Help message
"""

def menu():

	pr = Profiler()
	pr.loadDatabase(pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """
                         __..--.._ 
  .....              .--~  .....  `.         Time:      [ %s | %s ]
.":    "`-..  .    .' ..-'"    :". `         Author:    [ HackErWaSi ]      
` `._ ` _.'`"(     `-"'`._ ' _.' '           Version:   [ %s ]              
     ~~~      `.          ~~~                Pays:      [ %s | %s ]
              .'                             Database:  [ %s | %s Ko ]  
             /                             
            (                             %s
             ^---'                                                                                  
	""" % (Fore.YELLOW+str(today_date)+Fore.RESET, Fore.YELLOW+times()+Fore.RESET, 
		   Fore.YELLOW+str(__version__)+Fore.RESET, 
		   Fore.CYAN+monpays+Fore.RESET, codemonpays,
		   Fore.GREEN+str(nbProfilesBDD)+Fore.RESET, Fore.RED+str(sizeOfDB)+Fore.RESET,
		   random.choice(text)
		  )
	
	print(lb_header())
	print(menu)

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n HackErWaSi("+Fore.BLUE + "~" + Fore.RESET + ")$ ")
	
		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = Profiler()
				pr.loadDatabase(pathDatabase)
				database = pr.database
				
				choix = input("\n HackErWaSi("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

				if choix.lower() == 'h':
					print(helpMsg)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e':
					sys.exit("\n"+information+" Bye ! :)")
				elif choix.lower() == "1":
					profile = input(" Profil: ")
					data = pr.searchDatabase(profile, database=database)
					profilerFunc(data, path=pathDatabase)
					
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: Prenom Nom)"+Fore.RESET)
					name = input(" Nom du Profil: ")
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					twitter = input(" Twitter: ")
					# print(found+" %s" % (twitter))
					instagram = input(" Instagram: ")
					# print(found+" %s" % (instagram))
					facebook = input(" Facebook: ")
					# print(found+" %s" % (facebook))

					info = {"URL": {"Twitter": twitter, "Facebook":facebook, "Instagram": instagram}}
					create = pr.writeProfile(fileName=name, path=pathDatabase, info=info)

					if create:
						print("\n"+found+" Le profil '%s' a été créé avec succès." % (name))
					else:
						print("\n"+warning+" Une erreur est survenue. Le profil '%s' n'a pas pu être créé." % (name))

		elif choix.lower() == 'e':
			sys.exit("\n"+information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n HackErWaSi("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '4':
					searchNumber(codemonpays)
				elif lookup.lower() == '7':
					SearchEmail()
				#  ...
				elif lookup.lower() == '3':
					searchAdresse(codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Commande introuvable")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n HackErWaSi("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n HackErWaSi("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					codemonpays = "FR"
					monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					codemonpays = "BE"
					monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					codemonpays = "CH"
					monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					codemonpays = "LU"
					monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					codemonpays = "XX"
					monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMsg)
		else:
			pass
			# print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")