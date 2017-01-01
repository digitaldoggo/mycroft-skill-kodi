import helpers

searchBy = {
    'name': 'title',
    'category': 'genre',
    'recent': 'dateadded'
}

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
        
def GetMoviesBySearch(conn, getBy, searchTerm, start=0):
    if searchBy.has_key(getBy.lower()):
        method = 'VideoLibrary.GetMovies'
        json_params = {
            'jsonrpc':'2.0',
            'method':method,
            'id':15,
            'params': {
                'properties': [],
                'limits': {
                    'start': start,
                    'end': start + 3
                },
                'sort': {
                    'order': 'ascending',
                    'method': 'title',
                    'ignorearticle': True
                },
                'filter': {
                    'field': searchBy[getBy.lower()],
                    'operator': 'contains',
                    'value': searchTerm
                }
            }
        }
    else:
        return {
            'error': 'Unable to search by ' + getBy + '.'
        }
    res = helpers.make_request(conn, method, json_params)
    if (res.has_key('result') and
        res['result'].has_key('movies') and
        len(res['result']['movies']) > 0):
        movies = res['result']['movies']
        for i in range(0,len(movies)):
            return movies
    else:
        print 'No movies found matching your search for ' + searchTerm + '.'

def PlayMovieById(conn, movieid):
    method = 'Player.Open'
    json_params = {
        'jsonrpc':'2.0',
        'method':method,
        'id':1,
        'params': {
            'item':{
                'movieid': movieid
            }
        }
    }
    res = helpers.make_request(conn, method, json_params)