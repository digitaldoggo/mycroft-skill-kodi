from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import httplib2
import json

__author__ = 'k3yb0ardn1nja'

LOGGER = getLogger(__name__)


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
        conn = httplib2.Http(".cache")
        method = "Player.PlayPause"
        json_params = json.dumps({
            "jsonrpc":"2.0",
            "method":method,
            "id":1,
            "params": {
                "playerid":1
            }
        })
        headers = {
            "Content-type": "application/json",
        }
        res, c = conn.request("http://localhost:8080/jsonrpc?" + method, 'POST', json_params, headers)
        print json.dumps(res)
        pass
        

    def stop(self):
        pass


def create_skill():
    return PauseSkill()