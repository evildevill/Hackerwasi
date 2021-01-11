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
		sys.exit(warning+" please install python3 to use this tool.")

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
	chaine = "[*]"+' Start Hacker wasi...'
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

	string = "Start Hacker wasii😘"
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
	string = "Start Hackerwasi..."

	while importlib.is_alive():

		space = " " * 100
		sys.stdout.write("\r"+space)
		
		x = 1

		while x <= len(string):
			times = "0."
			times += str(random.choice(range(1, 3)))
			sys.stdout.write("\rroot@Hackerwasi:~$ "+string[:x]+"|")
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
 _    _    __    ___  ____ 
( \/\/ )  /__\  / __)(_  _)
 )    (  /(__)\ \__ \ _)(_ 
(__/\__)(__)(__)(___/(____)
"""

header2 = """
 _  _   __   ____  __  
/ )( \ / _\ / ___)(  ) 
\ /\ //    \\___ \ )(  
(_/\_)\_/\_/(____/(__) 
"""

header5 = """
 __      __               .__ 
/  \    /  \_____    _____|__|
\   \/\/   /\__  \  /  ___/  |
 \        /  / __ \_\___ \|  |
  \__/\  /  (____  /____  >__|
       \/        \/     \/    
"""

header6 = """
 __    __          _ 
/ / /\ \ \__ _ ___(_)
\ \/  \/ / _` / __| |
 \  /\  / (_| \__ \ |
  \/  \/ \__,_|___/_|
"""

header7 = """
  _      __         _ 
 | | /| / /__ ____ (_)
 | |/ |/ / _ `(_-</ / 
 |__/|__/\_,_/___/_/  
"""

header8 = """
,--.   ,--.               ,--. 
|  |   |  | ,--,--. ,---. `--' 
|  |.'.|  |' ,-.  |(  .-' ,--. 
|   ,'.   |\ '-'  |.-'  `)|  | 
'--'   '--' `--`--'`----' `--' 
"""

header9 = """
 __        __        _ 
 \ \      / /_ _ ___(_)
  \ \ /\ / / _` / __| |
   \ V  V / (_| \__ \ |
    \_/\_/ \__,_|___/_|
"""

header11 = """
 ,--.   ,--.               ,--. 
 |  |   |  | ,--,--. ,---. `--' 
 |  |.'.|  |' ,-.  |(  .-' ,--. 
 |   ,'.   |\ '-'  |.-'  `)|  | 
 '--'   '--' `--`--'`----' `--' 
"""

header12 = """
,--.   ,--.               ,--. 
|  |   |  | ,--,--. ,---. `--' 
|  |.'.|  |' ,-.  |(  .-' ,--. 
|   ,'.   |\ '-'  |.-'  `)|  | 
'--'   '--' `--`--'`----' `--' 
"""

header13 = """
   __     __     ______     ______     __    
  /\ \  _ \ \   /\  __ \   /\  ___\   /\ \   
  \ \ \/ ".\ \  \ \  __ \  \ \___  \  \ \ \  
   \ \__/".~\_\  \ \_\ \_\  \/\_____\  \ \_\ 
    \/_/   \/_/   \/_/\/_/   \/_____/   \/_/ 
"""

header14 = """
 __ __ __   ________   ______    ________     
/_//_//_/\ /_______/\ /_____/\  /_______/\    
\:\\:\\:\ \\::: _  \ \\::::_\/_ \__.::._\/    
 \:\\:\\:\ \\::(_)  \ \\:\/___/\   \::\ \     
  \:\\:\\:\ \\:: __  \ \\_::._\:\  _\::\ \__  
   \:\\:\\:\ \\:.\ \  \ \ /____\:\/__\::\__/\ 
    \_______\/ \__\/\__\/ \_____\/\________\/ 
"""

header15 = """
.-.  .-.  .--.     .---. ,-. 
| |/\| | / /\ \   ( .-._)|(| 
| /  \ |/ /__\ \ (_) \   (_) 
|  /\  ||  __  | _  \ \  | | 
|(/  \ || |  |)|( `-'  ) | | 
(_)   \||_|  (_) `----'  `-' 
"""

header16 = """
 ____      ____              _   
|_  _|    |_  _|            (_)  
  \ \  /\  / /,--.   .--.   __   
   \ \/  \/ /`'_\ : ( (`\] [  |  
    \  /\  / // | |, `'.'.  | |  
     \/  \/  \'-;__/[\__) )[___] 
"""

header17 = """

 ___       __   ________  ________  ___     
|\  \     |\  \|\   __  \|\   ____\|\  \    
\ \  \    \ \  \ \  \|\  \ \  \___|\ \  \   
 \ \  \  __\ \  \ \   __  \ \_____  \ \  \  
  \ \  \|\__\_\  \ \  \ \  \|____|\  \ \  \ 
   \ \____________\ \__\ \__\____\_\  \ \__\
    \|____________|\|__|\|__|\_________\|__|
                            \|_________| 
"""

header18 = """
██╗    ██╗ █████╗ ███████╗██╗
██║    ██║██╔══██╗██╔════╝██║
██║ █╗ ██║███████║███████╗██║
██║███╗██║██╔══██║╚════██║██║
╚███╔███╔╝██║  ██║███████║██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝
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
 [1]  Personne lookup                  Research with a name, first name and (city).
 [2]  Username lookup                  Research with a pseudonym.
 [3]  Adresse lookup                   Search with an address.
 [4]  Phone lookup                     Research with a phone number.
 [5]  IP lookup                        Searching with an IP address.
 [6]  SSID locator                     Searching with a MAC / BSSID address
 [7]  Email lookup                     Research with an email address.
 [8]  Mail tracer                      Research with the header of an email.
 [9]  Employés recherche               Finds the employees of a company.
 [10] Google search                    Research on google.
 [11] Facebook graphSearch             Research using graphSearch.
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

text = ['Press F to hack', ' Hacekr wasii', 'Best OSINT Tool', 'Pakistan black Mafia', 'Twitter: Hackerwasii', 'insta : Hackerwasii', 'website : hackerwasii.com', 'BlackHat Hacker', 'Waseem Akram']

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
.":    "`-..  .    .' ..-'"    :". `         Author:    [ Waseem Akram ]      
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
		choix = input("\n Hackerwasii("+Fore.BLUE + "~" + Fore.RESET + ")$ ")
	
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
				
				choix = input("\n Hackerwasi("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

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
					sys.exit("\n"+information+" Bye Thanks for using! :)")
				elif choix.lower() == "1":
					profile = input(" Profile: ")
					data = pr.searchDatabase(profile, database=database)
					profilerFunc(data, path=pathDatabase)
					
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: First name Last name)"+Fore.RESET)
					name = input(" Profile Name: ")
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
						print("\n"+found+" Profile '% s' was created successfully." % (name))
					else:
						print("\n"+warning+" An error has occurred. Profile '% s' could not be created. please Try again😘" % (name))

		elif choix.lower() == 'e':
			sys.exit("\n"+information+" Bye Keep supporting guys😍😘! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n Hackerwasii("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
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
				se = input("\n Hackerwasii("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
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
					sys.exit("\n"+information+" Bye Thanks my friend for using our Tool 😘😍♥️! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n Hackerwasii("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
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
	sys.exit("\n"+information+" Bye ALLAH HAFIZ 🥰😍♥️! :)")
