import os.path
from netifaces import interfaces, ifaddresses, AF_INET
import httplib2
import json
import socket
import jsonhelpers

headers = {"Content-type": "application/json"}

configFile = 'mycroft/configuration/kodi-config.json'
# testing
configFile = 'kodi-config.json'

def make_request(conn, method, json_params):
    config = auto_discover()
    if config == -1:
        return -1
    try:
        res, c = conn.request('http://' + config['HOST'] + ':' + str(config['PORT']) + '/jsonrpc?' + method, 'POST', json.dumps(json_params), headers)
        
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
        
def auto_discover():
    # TODO: use async requests
    conn = httplib2.Http(timeout=.1)
    method = 'XBMC.GetInfoLabels'
    json_params = {
        'jsonrpc':'2.0',
        'method':method,
        'id':1,
        'params': [['Network.IPAddress','System.FriendlyName']]
    }
    
    if os.path.isfile(configFile):
        with open(configFile) as data_file:
            config = jsonhelpers.json_load_byteified(data_file)
    
    if ('config' in locals() and
        config.has_key('HOST') and
        config.has_key('PORT')):
        try:
            res, c = conn.request('http://' + config['HOST'] + ':' + str(config['PORT']) + '/jsonrpc?' + method, 'POST', json.dumps(json_params), headers)
            if ('res' in locals() and
                res.has_key('status') and
                res['status'] == '200'):
                print('Using config in ' + configFile)
                return config
            else:
                print("Reconfiguring")
        except:
            print("Reconfiguring")
    
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        if ifaceName != "lo":
            for xxx in range(1, 255):
                try:
                    ipPrefix = addresses[0][:addresses[0].rfind('.') + 1]
                
                    res, c = conn.request('http://' + ipPrefix + str(xxx) + ':8080/jsonrpc?' + method, 'POST', json.dumps(json_params), headers)
                    
                    if hasattr(res, 'status'):
                        status = res['status']
                    else:
                        print("Response received, but no status.")
                        return -1
                    
                    if status == '200':
                        if 'c' in locals():
                            result = jsonhelpers.json_loads_byteified(c)
                            if result.has_key('error'):
                                print("Error received from Kodi")
                                return -1
                            elif 'result' in locals():
                                print("Kodi found at 10.10.1." + str(xxx))
                                if 'config' in globals():
                                    config['NAME'] = result['result']['System.FriendlyName']
                                    config['HOST'] = result['result']['Network.IPAddress']
                                    config['PORT'] = 8080
                                else:
                                    f = open(configFile, 'w+')
                                    config = {
                                        'NAME': result['result']['System.FriendlyName'],
                                        'HOST': result['result']['Network.IPAddress'],
                                        'PORT': 8080
                                    }
                                    f.writelines([
                                        '{',
                                        '\n\t"NAME":"' + result['result']['System.FriendlyName'] + '",',
                                        '\n\t"HOST":"' + result['result']['Network.IPAddress'] + '",',
                                        '\n\t"PORT":' + '8080',
                                        '\n}'
                                    ])
                                return config
                    print("Response received, but there was an issue. Status: " + status)
                    return -1
                except socket.error, err:
                    pass
                except:
                    pass
    return -1
