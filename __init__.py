from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import httplib2
import json

with open('constants.json') as data_file:
    constants = json.load(data_file)

import helpers

__author__ = 'k3yb0ardn1nja'

LOGGER = getLogger(__name__)

# TODO: rename to KodiSkill and handle intents within or make multiple skills?
class PauseSkill(MycroftSkill):
    def __init__(self):
        super(PauseSkill, self).__init__(name="PauseSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        intent = IntentBuilder("PauseSkill").require("PauseKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        #self.speak("Play Videos.")
        print "Playing the movie."
        
        conn = httplib2.Http()

        playerid = helpers.get_player_id(conn)
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
            res = helpers.make_request(conn, method, json_params)
            
        elif playerid == 0:
            print "There is no player"
            
        else:
            print "An error occurred"
            
        pass
        

    def stop(self):
        pass


def create_skill():
    return PauseSkill()