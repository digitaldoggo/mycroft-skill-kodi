import helpers

def PlayPause(conn):
    playerid = helpers.get_player_id(conn)

    if playerid > 0:
        method = 'Player.PlayPause'
        json_params = {
            'jsonrpc':'2.0',
            'method':method,
            'id':1,
            'params': {
                'playerid':playerid
            }
        }
        res = helpers.make_request(conn, method, json_params)
        
    elif playerid == 0:
        print 'There is no player'
        
    else:
        print 'An error occurred'
        
def Stop(conn):
    playerid = helpers.get_player_id(conn)

    if playerid > 0:
        method = 'Player.Stop'
        json_params = {
            'jsonrpc':'2.0',
            'method':method,
            'id':1,
            'params': {
                'playerid':playerid
            }
        }
        res = helpers.make_request(conn, method, json_params)
        
    elif playerid == 0:
        print 'There is no player'
        
    else:
        print 'An error occurred'
        
def GetPlayerItem(conn):   
    playerid = helpers.get_player_id(conn)

    if playerid > 0:
        method = 'Player.GetItem'
        json_params = {
            'jsonrpc':'2.0',
            'method':method,
            'id':1,
            'params': {
                'playerid':playerid
            }
        }
        res = helpers.make_request(conn, method, json_params)
        if (res.has_key('result') and
           res['result'].has_key('item') and
           res['result']['item'].has_key('label')):
            print(res['result']['item']['label'])
        else:
            print 'An error occurred'
        
    elif playerid == 0:
        print 'There is no player'
        
    else:
        print 'An error occurred'