import httplib2
import json

import helpers
import kodicontrols

conn = httplib2.Http()
# caches stuff retrieved (use for searching)
#connection = httplib2.Http(".cache")

#kodicontrols.GetPlayerItem(conn)
#kodicontrols.PlayPause(conn)
#kodicontrols.Stop(conn)
#helpers.auto_discover()
res = kodicontrols.GetMoviesBySearch(conn, 'name', 'Lord of the Rings the two towers')

if (type(res) is dict and
    res.has_key('error')):
    print(res['error'])
else:
    if (res is not None):
        if(res.count > 1):
            kodicontrols.PlayMovieById(conn, res[0]['movieid'])