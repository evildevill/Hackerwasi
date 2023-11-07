import requests
from core.searchPJ import searchPJ
from core.searchInfoNumero import searchInfoNumero
from core.searchYellowLU import searchYellowLU
from core.searchLocalCH import searchLocalCH
from core.searchPageDor import searchPageDor
from core.facebookSearchTool import facebookSearchTool
from core.twitterSearchTool import twitterSearchTool
from core.instagramSearchTool import instagramSearchTool
from core.searchCopainsdavant import searchCopainsdavant
from core.searchPersonneLinkedin import searchPersonneLinkedin
from terminaltables import SingleTable
from colorama import init, Fore,  Back,  Style

warning = "[" + Fore.RED + "!" + Fore.RESET + "]"
question = "[" + Fore.YELLOW + "?" + Fore.RESET + "]"
found = "[" + Fore.GREEN + "+" + Fore.RESET + "]"
wait = "[" + Fore.MAGENTA + "*" + Fore.RESET + "]"

init()

def searchPersonne(codemonpays):
    nom = input(" Name, First Name: ")
    city = input(" City/Department: ")
    print("\n" + wait + " Searching...")

    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'referrer': 'https://google.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'utf-8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Pragma': 'no-cache'
        }

        if codemonpays == 'FR':
            # Yellow Pages search
            url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
            request = requests.get(url.format(nom, city), headers=headers)
            searchPJ(request)
        elif codemonpays == 'BE':
            # Yellow Pages search for Belgium
            url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
            request = requests.get(url.format(nom, city), headers=headers)
            searchPageDor(request)
        elif codemonpays == 'CH':
            # Swiss search
            url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
            searchLocalCH(url.format(city, nom))
        elif codemonpays == 'LU':
            # Luxembourg search
            url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}"
            searchYellowLU(url.format(nom))
        else:
            # Default to French search
            url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
            request = requests.get(url.format(nom, city), headers=headers)
            searchPJ(request)
            url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
            request = requests.get(url.format(nom, city), headers=headers)
            searchPageDor(request)
            url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
            searchLocalCH(url.format(city, nom))
            url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}"
            searchYellowLU(url.format(nom))

        # Search for old friends
        searchCopainsdavant(nom, city)

        # LinkedIn search
        searchPersonneLinkedin(nom, city)

        # Facebook search
        fbtool = facebookSearchTool()
        accountsFb = fbtool.searchFacebook(nom)

        title = " Facebook "
        TABLE_DATA = [
            ('Name', 'User', 'Location'),
        ]
        count = 0
        for a in accountsFb:
            count += 1
            name = a[1]
            username = a[0]
            fbtool.getInfoProfile(username)
            loc = fbtool.address
            if not loc:
                loc = ""
            tuples = (name, username, loc)
            TABLE_DATA.append(tuples)

        if count > 0:
            table_instance = SingleTable(TABLE_DATA, title)
            print(table_instance.table)

        # Twitter search
        title = " Twitter "
        TABLE_DATA = [
            ('Name', 'User', 'Date', 'Location'),
        ]
        twitool = twitterSearchTool()
        accountTwitter = twitool.searchTwitter(nom)
        count = 0
        for a in accountTwitter:
            count += 1
            name = a[1]
            username = "@" + a[0]
            twitool.getInfoProfile(a[0])
            location = twitool.location
            date = twitool.birth
            bio = twitool.description
            url = twitool.url
            tuples = (name, username, date, location)
            TABLE_DATA.append(tuples)

        if count > 0:
            table_instance = SingleTable(TABLE_DATA, title)
            print(table_instance.table)

        # Instagram search
        title = " Instagram "
        instatls = instagramSearchTool()
        instatls.searchInsta(nom)
        accounts = instatls.accounts
        TABLE_DATA = [
            ('Name', 'User'),
        ]
        count = 0
        for account in accounts:
            url = "https://instagram.com/" + account
            i = instagramSearchTool()
            i.getInfo(url)
            name = i.name
            tuples = (name, account)
            TABLE_DATA.append(tuples)
            count += 1

        if count > 0:
            table = SingleTable(TABLE_DATA, title)
            print(table.table)
    except IOError:
        pass