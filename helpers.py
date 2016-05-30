import httplib2
import json
import socket

import jsonhelpers

with open('config.json') as data_file:
    config = json.load(data_file)
# TODO: check config. auto-discover and update config if needed
# try simple request to assure kodi is present, then
# auto-discover and update config if not

with open('constants.json') as data_file:
    constants = jsonhelpers.json_load_byteified(data_file) 

def make_request(conn, method, json_params):
    try:
        res, c = conn.request('http://' + config['HOST'] + ':' + config['PORT'] + '/jsonrpc?' + method, 'POST', json.dumps(json_params), constants['headers'])
        
        if hasattr(res, 'status'):
            status = res['status']
        else:
            return -1
        
        if status == '200':
            if 'c' in locals():
                result = jsonhelpers.json_loads_byteified(c)
                if result.has_key('error'):
                    # TODO: better handle errors returned from kodi
                    return -1
                elif 'result' in locals():
                    return result
        return -1
    # TODO: better handle errors caught from request attempt
    except socket.error, err:
        return -1
    except httplib2.ServerNotFoundError:
        return -1


def get_player_id(conn):
    method = 'Player.GetActivePlayers'
    json_params = {
        'jsonrpc':'2.0',
        'method':method,
        'id':1
    }
    result = make_request(conn, method, json_params)
    
    if result == -1:
        return -1
    elif result['result'] != [] and result['result'][0].has_key('playerid'):
        return result['result'][0]['playerid']
    else:
        return 0