from os.path import dirname
import httplib2
import json

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.skills.kodi_controller.helpers import get_player_id
from mycroft.skills.kodi_controller.helpers import make_request

__author__ = 'k3yb0ardn1nja'

LOGGER = getLogger(__name__)

# TODO: rename to KodiSkill and handle intents within or make multiple skills?
class KodiSkill(MycroftSkill):
    def __init__(self):
        super(KodiSkill, self).__init__(name="KodiSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        playpause_intent = IntentBuilder("PlayPause").require("PlayPauseKeyword").build()
        self.register_intent(playpause_intent, self.handle_playpause_intent)
        
        stop_intent = IntentBuilder("Stop").require("StopKeyword").build()
        self.register_intent(stop_intent, self.handle_stop_intent)

    def handle_playpause_intent(self, message):
        #self.speak("Play Videos.")
        conn = httplib2.Http()

        playerid = get_player_id(conn)
        if playerid > 0:
            method = "Player.PlayPause"
            json_params = {
                "jsonrpc":"2.0",
                "method":method,
                "id":1,
                "params": {
                    "playerid":playerid
                }
            }
            res = make_request(conn, method, json_params)
            
        elif playerid == 0:
            print "There is no player"
            
        else:
            print "An error occurred"
        pass
    
    def handle_stop_intent(self, message):
        #self.speak("Play Videos.")
        conn = httplib2.Http()

        playerid = get_player_id(conn)
        if playerid > 0:
            method = "Player.Stop"
            json_params = {
                "jsonrpc":"2.0",
                "method":method,
                "id":1,
                "params": {
                    "playerid":playerid
                }
            }
            res = make_request(conn, method, json_params)
            
        elif playerid == 0:
            print "There is no player"
            
        else:
            print "An error occurred"
        pass

def create_skill():
    return KodiSkill()