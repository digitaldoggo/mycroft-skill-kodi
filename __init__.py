from os.path import dirname
import httplib2
import json

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.skills.kodi_controller.helpers import *
from mycroft.skills.kodi_controller.kodicontrols import *

__author__ = 'k3yb0ardn1nja'

LOGGER = getLogger(__name__)

class KodiSkill(MycroftSkill):
    def __init__(self):
        super(KodiSkill, self).__init__(name="KodiSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        playpause_intent = IntentBuilder("PlayPause").require("PlayPauseKeyword").build()
        self.register_intent(playpause_intent, self.handle_playpause_intent)
        
        stop_intent = IntentBuilder("Stop").require("StopKeyword").build()
        self.register_intent(stop_intent, self.handle_stop_intent)
        
        pick_movie_intent = IntentBuilder("PickMovie").require("PickMovieKeyword").require("Movie").build()
        self.register_intent(pick_movie_intent, self.handle_pick_movie_intent)
        
    def handle_playpause_intent(self, message):
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
            self.speak("There is no open video")
            
        else:
            self.speak("An error occurred")
            
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
            self.speak("There is no open video")
            
        else:
            self.speak("An error occurred")
            
        pass

    def handle_pick_movie_intent(self, message):
        conn = httplib2.Http()
        search = message.data.get("Movie")

        res = GetMoviesBySearch(conn, 'name', search)
        if (type(res) is dict and
            res.has_key('error')):
            print(res['error'])
        else:
            if (res is not None and
            len(res) > 0):
                speech = 'Playing ' + res[0]['label'] + ' on Kodi.'
                PlayMovieById(conn, res[0]['movieid'])
                # speech = 'I found ' + str(len(res)) + ' movies matching your search for ' + search + '... '
                # for i in range(0,3):
                #     speech += res[i]['label'] + ' , , '
                # speech += 'Were you looking for one of these?'
            else:
                speech = 'I couldn\'t find a movie matching your search for ' + search + '.'
            self.speak(speech)

def create_skill():
    return KodiSkill()