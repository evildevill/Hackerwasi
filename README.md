## Thank You-🙏🏼

<p>
<img src="https://visitor-badge.laobi.icu/badge?page_id=HackerWaSi" alt="visitor badge"/>
</p>

<img src="https://github.com/evildevill/Hackerwasi/blob/master/images/s1png">

Table of Contents

* [Hackerwasii](#Hackerwasii)
* [Disclaimer](#Disclaimer)
* [Installation on Linux](#Installation-on-Linux)
* [Installation on Windows](#Installation-on-Windows)
* [Contributors](#Contributors)
* [Support us](#Support-us)

Hackerwasi is an information collection tool (OSINT) which aims to carry out research on a French, Swiss, Luxembourgish or Belgian person. It provides various modules that allow efficient searches. HaCkeRWaSi does not require an API key or login ID.

![]()

Disclaimer
=
Hackerwasi was developed to do research on yourself and to see private and sensitive information that can be left behind on social media. I do not in any way encourage the use of this tool on anyone other than yourself or to misuse this tool. The authors of HaCkeRWaSi cannot be held responsible for the use of its tool.

Installation on Linux
=
You must have `git` and` python3` to install on your machine
```
    sudo apt install git python3 #on distributions using APT (like the Debian family)
    git clone https://github.com/evildevill/Hackerwasi
    cd Hackerwasi
    python3 -m pip install -r requirements.txt
```    

Execution Linux
=
In the Hackerwasi directory, run this command to be able to launch Hackerwasi:
```
python3 Hackerwasi.py
```
### Screen Shots
 <img src="https://github.com/evildevill/Hackerwasi/blob/master/images/s3.png">
 
 
### Installation on Termux
```
    pkg update -y
    pkg upgrade -y
    pkg instal python2 -y
    pkg install python -y
    pkg install git -y
    git clone https://github.com/evildevill/Hackerwasi
    cd Hackerwasi
    chmod +x *
    pip3 install -r requirements.txt
    or
    python -m pip install -r requirements.txt
    python Hackerwasi.py

```

Installation on Windows
=
- 1. Download [Hackerwasi](https://github.com/evildevill/Hackerwasi/archive/master.zip)
- 2. Install Python from the Windows Store
- 4. unzip Hakerwasii (master.zip)
- 5. Open `CMD` and go to the **` Hackerwasii-master` ** directory using the `cd` command.
     Eg:
```
cd Desktop\
cd Hackerwasi-master\
``` 
execute:
```
    python3 -m pip install -r requirements.txt
```
<img src="https://github.com/evildevill/Hackerwasi/blob/master/images/s2.png">
<img src="https://github.com/evildevill/Hackerwasi/blob/master/images/s4.png">
<img src="https://github.com/evildevill/Hackerwasi/blob/master/images/s5.png">
<img src="https://github.com/evildevill/Hackerwasi/blob/master/images/s6.png">
Start Hackerwasii from Windows:
=
- Go to the ** Hackerwasi-master ** directory as when it was installed and run the command:
`` ``
python3 Hackerwasi.py
```

Discord
=
~~ If you have any questions, ideas, issues regarding HaCkeRWaSi or if you just want to follow the progress of this project. ~~
Momentarily closed.

New in version 6.0
=
- In addition (+)
- A 'requirements.txt' file has been added.
- A new interface.
- A new OSINT module has been added. The 'Profiler' module allows you to create a profile and retrieve information on the sites defined by the user, save this data and display the last posts published on the networks (filtered according to the publication dates).
	- New search services (Directories) have been added depending on the user's location. HaCkeRWaSi uses your IP to determine the country you are in. Under no circumstances will your IP or other private information be shared. You can choose a country other than your own to centralize your searches.
- Instagram and LinkedIn search integrated with 'Person Lookup'.
- A new 'Employees search' module which allows you to find people via a company and a city.
- Instagram and Facebook information search modules have been improved to extract more information.

- In less (-)
- Some python libraries (dnspython, socket and smtplib) have been removed for this version.
- 'Social engineering tool' has been modified for 'Other tool' it only includes the brute force module of a Hash.
- The 'Spam Email' and 'SMS' modules have been removed from HaCkeRWaSi.


Compatible
=
- Windows
- MacOS
- Linux

Python version:
=
- Python3

Modules Python
=
- requests
- bs4
- terminaltables
- colorama

Fonctionnalites
=
 - Lookup:
	- Phone lookup
	- Email lookup
	- Last name / First name lookup
	- Surname lookup
	- Addresse lookup
	- Mail ip locator
	- Ip locator
	- Bssid locator
	- Exif read
	- Google search
	- Twitter
	- Instagram
	- Facebook
	- LinkedIn employee search (New !)
	- Hash Bruteforce (New !)

 - Autre outils:

	- Hash Bruteforce

- Profiler (New !)
	- Profiler an profile
	- Database management
	- Profile creator
