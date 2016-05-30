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