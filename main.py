#!/usr/bin/env python
import sys
import urllib2
import time
import git
from shutil import copyfile
import json
import requests
import subprocess

with open('gmcu.json') as json_file:
    data = json.load(json_file)
    # GeyserMC Plugin Information
    geyser_ver = (data['GeyserMcInfo']['version'])
    geyser_loc = (data['GeyserMcInfo']['location'])
    geyser_dlfile = (data['GeyserMcInfo']['downloadfile'])
    # Server Information
    geyser_startup = (data['ServerInfo']['startup-script'])
    autoupdater_prompt = (data['ServerInfo']['prompt-before-autoupdater-update'])
    geyser_prompt = (data['ServerInfo']['prompt-before-geyser-update'])
    # Dynamic Information (this information changes, such as version numbers)
    geyser_lsb = (data['DynamicInfo']['geyserlsb'])
    autoupdater_lsb = (data['DynamicInfo']['updaterlsb'])
# CHECK FOR REQUIREMENTS
# Make sure Python is 2.7
version = sys.hexversion
if sys.hexversion != 34017264:
    print "This script requires Python version 2.7. You are not running 2.7"
    sys.exit(1)
# Check for Python Updates
currentbuild = 0
geyser_current = urllib2.urlopen('https://raw.githubusercontent.com/michaelwatne/geysermcupdater/master/.VERSION')
latestbuild = geyser_current.read()
latestbuild = latestbuild.replace('\n', '')

if autoupdater_lsb == latestbuild:
    print "You\'re running the latest version of Geyser MC Updater:", autoupdater_lsb
else:
    # if there is a new version, ask to update
    print "A new version of the Auto Updater is available. It\'s recommended that you download the latest version."
    if autoupdater_prompt == "yes":
        getanswer = raw_input('Would you like to download the latest version? [Y/n]')
    else:
        getanswer = "y"
    if getanswer == 'y' or getanswer == 'Y':
        print "Downloading new version..."
        git.Git("").clone("https://github.com/michaelwatne/geysermcupdater.git")
        print "Copying auto-updater files to working directory..."
        src = "geysermcupdater/main.py"
        dst = "main.py"
        copyfile(src, dst)
        src = "geysermcupdater/.VERSION"
        dst = ".VERSION"
        copyfile(src, dst)
        with open("gmcu.json", "r") as jsonfile:
            data = json.load(jsonfile)
        data['DynamicInfo']['updaterlsb'] = latestbuild
        with open("gmcu.json", "w") as jsonfile:
            json.dump(data, jsonfile)
        print "Auto updater needs to reload. Will automatically reload in 10 seconds.."
        time.sleep(10)
        execfile("./main.py")
        sys.exit(0)
time.sleep(2)
# Start Updater
print "GEYSER AUTO UPDATER. VERSION", autoupdater_lsb
print "THIS PROGRAM IS IN NO WAY, ASSOCIATED WITH GEYSER MC, AND MAY COME WITH OCCASIONAL BUGS! THIS PROGRAM IS\n\
\"AS IS\" WITHOUT WARRANTY, AND DEVELOPERS OF THIS PROGRAM MAY NOT BE HELD RESPONSIBLE OR LIABLE FOR ANY DAMAGES\n\
TO YOUR FILES OR SOFTWARE! THIS PROGRAM SHOULD NOT RUN OUTSIDE ITS ENVIRONMENT, AND IT IS STRONGLY SUGGESTED\n\
YOU BACKUP ANY FILES BEFORE USING THIS SCRIPT!"
time.sleep(5)
# Grab Geyser Information
print "Getting information about your version of Geyser..."
try:
    verifyloc = open(geyser_loc)
    print "Found", geyser_ver, "at", geyser_loc
except IOError:
    print "We tried looking for", geyser_loc, "but we couldn\'t find it. Verify this file exists and make sure"
    print "gmcu.json has the updated location."
    sys.exit(1)
finally:
    verifyloc.close()
# Check if Geyser is latest version
print "Checking if", geyser_ver, "is the latest version..."

req = urllib2.Request('https://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/buildNumber',
                      headers={'User-Agent': "Magic Browser"})
lsbcheck = urllib2.urlopen(req)
lsb = lsbcheck.read()
if lsb == geyser_lsb:
    print "Your version of geyser is the latest version."

else:
    print "Web:", lsb, "Current:", geyser_lsb
    print "A new version of", geyser_ver, "is available!"
    if geyser_prompt == "yes":
        getanswer2 = raw_input('Would you like to download the latest version? [Y/n]')
    else:
        getanswer2 = "y"
    if getanswer2 == 'y' or getanswer2 == 'Y':
        print "Downloading new version..."
        downloadurl = "https://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/" + geyser_ver + "/target/" + geyser_dlfile
        request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://thewebsite.com",
            "Connection": "keep-alive"
        }
        download = requests.get(downloadurl, headers=request_headers)
        open(geyser_loc, 'wb').write(download.content)
        print "Updating version ID..."
        with open("gmcu.json", "r") as jsonfile:
            data = json.load(jsonfile)
        data['DynamicInfo']['geyserlsb'] = lsb
        with open("gmcu.json", "w") as jsonfile:
            json.dump(data, jsonfile)
print "Done! Running your startup script"

subprocess.call(geyser_startup)
exit(0)
