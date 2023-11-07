#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style
from lib.menu import checkVersion, clear, menu
from lib.loading import thread_loading
#Lookup Menu
from core.searchEmail import SearchEmail
from core.searchPersonne import searchPersonne
from core.searchAdresse import searchAdresse
from core.searchUserName import searchUserName
from core.ipFinder import ipFinder
from core.bssidFinder import bssidFinder
from core.mailToIP import mailToIP
from core.employee_lookup import employee_lookup
from core.google import google
from core.facebookStalk import facebookStalk
from core.searchTwitter import searchTwitter
from core.searchInstagram import searchInstagram
from core.profilerFunc import profilerFunc
from core.searchNumber import searchNumber
#Other tool menu
from core.hashDecrypt import hashdecrypt

#Help & settings
from txt.help import *
import settings

init()
settings.init()

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"

checkVersion()
thread_loading()

mainOption = """
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Change country
 [e] Exit script    [h] Help Message    [c] Clear Screen"""

lookupOption = """
 [1] Person lookup          [8] Mail tracer
 [2] Username lookup          [9] Employee search
 [3] Address lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearch
 [5] IP lookup                [12] Twitter info
 [6] SSID locator             [13] Instagram info
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
 [2] BE (Belgium)   [5] All (FR, BE, CH, LU)
 [3] CH (Switzerland)
 [b] back main menu   [c] Clear screen   [h] Help message
"""

clear()
menu()
print(mainOption)

try:
    while True:
        choix = input("\n Waseem Akram("+Fore.BLUE + "~" + Fore.RESET + ")$ ")

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
                pr = settings.Profiler()
                pr.loadDatabase(settings.pathDatabase)
                database = pr.database

                choix = input("\n Waseem Akram("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

                info = {"URL": {}}
                
                if choix.lower() == 'h':
                    print(helpProfiler)
                elif choix.lower() == 'b':
                    clear()
                    menu()
                    print(mainOption)
                    break
                elif choix.lower() == 'c':
                    clear()
                    menu()
                    print(profilerOption)
                elif choix.lower() == 'e' or choix.lower() == 'exit':
                    sys.exit("\n"+information+" Bye ! :)")
                elif choix.lower() == "1":
                    if pr.count >= 1:
                        while True: 
                            profile = input(" Profile: ")
                            if profile != '':
                                break
                        data = pr.searchDatabase(profile, database=database)
                        profilerFunc(data, path=settings.pathDatabase)
                    else:
                        print(warning+" No profile found. Please create one.")
                elif choix.lower() == "2":
                    pr.showAllProfiles(database=database)

                elif choix.lower() == '3':
                    print("\n"+Fore.YELLOW+"(Format: First name Last name)"+Fore.RESET)
                    while True: 
                        name = input(" Profile Name: ")
                        if name != '':
                            break
                    name = name.split(" ")
                    name = [i.capitalize() for i in name]
                    name = " ".join(name)
                    while True:
                        print(question+" Want to register a Twitter account to profile ?")
                        choixPr = input(" [Y/n]: " )
                        if choixPr.lower() == 'n':
                            break
                        else:
                            twitter = input("\n Twitter: ")
                            info['URL']['Twitter'] = twitter
                            break
                    # print(found+" %s" % (twitter))
                    while True:
                        print(question+" Want to register an Instagram account to profile ?")
                        choixPr = input(" [Y/n]: " )
                        if choixPr.lower() == 'n':
                            break
                        else:
                            instagram = input("\n Instagram: ")
                            info['URL']['Instagram'] = instagram
                            break
                    while True:
                        print(question+" want to register a Facebook account to profile ?")
                        choixPr = input(" [Y/n]: " )
                        if choixPr.lower() == 'n':
                            break
                        else:
                            facebook = input("\n Facebook: ")
                            info['URL']['Facebook'] = facebook
                            break

                    create = pr.writeProfile(fileName=name, path=settings.pathDatabase, info=info)

                    if create:
                        print("\n"+found+" Profile '%s' was created successfully." % (name))
                    else:
                        print("\n"+warning+" An error has occurred. Profile '%s' could not be created." % (name))

        elif choix.lower() == 'e' or choix.lower() == 'exit':
            sys.exit("\n"+information+" Bye ! :)")
        elif choix == '1':
            clear()
            menu()
            print(lookupOption)
            while True:
                lookup = input("\n Waseem Akram("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
                if lookup == 'h':
                    print(helpLookup)
                elif lookup.lower() == '1':
                    searchPersonne(settings.codemonpays)
                elif lookup.lower() == '2':
                    searchUserName()
                elif lookup.lower() == '3':
                    searchAdresse(settings.codemonpays)
                elif lookup.lower() == '4':
                    searchNumber(settings.codemonpays)
                elif lookup.lower() == '5':
                    ipFinder()
                elif lookup.lower() == '6':
                    bssidFinder()
                elif lookup.lower() == '7':
                    SearchEmail()
                elif lookup.lower() == '8':
                    mailToIP()
                elif lookup.lower() == '9':
                    employee_lookup()
                elif lookup.lower() == '10':
                    google()
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
                    # print("Command not found")
        elif choix == '2':
            clear()
            menu()
            print(otherToolOption)
            while True:
                se = input("\n Waseem Akram("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
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
                    # print("Command not found")
        elif choix == "4":
            clear()
            menu()
            print(countryMenu)

            while True:
                newCode = input("\n Waseem Akram("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
                if newCode == '1':
                    settings.codemonpays = "FR"
                    settings.monpays = "France"
                    clear()
                    menu()
                    print(mainOption)
                    break
                elif newCode == "2":
                    settings.codemonpays = "BE"
                    settings.monpays = "Belgium"
                    clear()
                    menu()
                    print(mainOption)
                    break
                elif newCode == '3':
                    settings.codemonpays = "CH"
                    settings.monpays = 'Switzerland'
                    clear()
                    menu()
                    print(mainOption)
                    break
                elif newCode == '4':
                    settings.codemonpays = "LU"
                    settings.monpays = "Luxembourg"
                    clear()
                    menu()
                    print(mainOption)
                    break
                elif newCode == '5':
                    settings.codemonpays = "XX"
                    settings.monpays = "Europe"
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
                    print(helpMain)
        else:
            pass
            # print("Command not found")

except KeyboardInterrupt:
    sys.exit("\n"+information+" Bye ! :)")
