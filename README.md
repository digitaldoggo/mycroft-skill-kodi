# Kodi Remote Control Skill for Mycroft

## Description
Mycroft skill to provide integration to Kodi (XBMC). Enables
the user to Play or Pause the currently playing video via voice
commands made to mycroft.

## Setup
1. Enable Web Server for remote control in Kodi's System Settings.
    - [Enabling Web Server](http://kodi.wiki/view/Settings/Services#Webserver)
    - Do not use a password
    - Use default port (8080)

2. Copy or clone this repository into mycroft's skills directory:
    ```
    git clone https://github.com/k3yb0ardn1nja/mycroft-skill-kodi /path/to/mycroft-core/mycroft/skills/kodi_controller
    ```

3. Run the setup script:
    ```
    cd kodi_controller
    sh ./setup.sh
    ```
    Note: if you are running mycroft in a virtual environment, be sure to run the setup script in the same environment. (workon mycroft)

## Usage
#### Examples:

    "mycroft, start the movie Rolling Kansas"
    "mycroft, start the movie Despicable"
    "mycroft, play the movie"
    "mycroft, play the video"
    "mycroft, pause the movie"
    "mycroft, pause the video"
    "mycroft, stop the movie"
    "mycroft, stop the video"
    "mycroft, close the movie"
    "mycroft, close the video"
    "mycroft, end the movie"
    "mycroft, end the video"