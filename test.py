import httplib2
import json

conn = httplib2.Http(".cache")
headers = {
    "Content-type": "application/json",
}

# Pause / Play
#
# method = "Player.PlayPause"
# json_params = json.dumps({
#     "jsonrpc":"2.0",
#     "method":method,
#     "id":1,
#     "params": {
#         "playerid":1
#     }
# })

# res = conn.request("http://localhost:8080/jsonrpc?" + method, 'POST', json_params, headers)


# Get movies
method = "Player.GetActivePlayers"
json_params = {
    "jsonrpc":"2.0",
    "method":method,
    "id":1
}

res = conn.request("http://localhost:8080/jsonrpc?" + method, 'POST', json.dumps(json_params), headers)

print(res[1])