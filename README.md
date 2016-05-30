# Kodi Remote Control Skill for Mycroft

## Description
Mycroft skill to provide integration to Kodi (XBMC)

## Setup
1. Enable Web Server for remote control in Kodi's System Settings.
    - [Enabling Web Server](http://kodi.wiki/view/Settings/Services#Webserver)
    - Do not use a password.
    - Use default port. (8080)

2. Copy or clone this repository into mycroft's skills directory:
```
git clone https://github.com/k3yb0ardn1nja/mycroft-skill-kodi /path/to/mycroft-core/mycroft/skills/kodi_skill 
```
3. Modify the vocab file to suit desires
```
vocab/en-us/KodiKeyword.voc
```