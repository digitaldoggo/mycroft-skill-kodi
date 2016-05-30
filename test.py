import httplib2
import json

import helpers
import kodicontrols

conn = httplib2.Http()
# caches stuff retrieved (use for searching)
#connection = httplib2.Http(".cache")

#kodicontrols.GetPlayerItem(conn)
kodicontrols.PlayPause(conn)
#kodicontrols.Stop(conn)
#helpers.auto_discover()