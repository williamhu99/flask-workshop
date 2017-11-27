import requests
import json
r = requests.get("https://api.github.com/events")
# print r.text
# converts to json dictionary
jsonified = r.json()

print len(jsonified)
push_event_ct = 0
other_event_ct = 0
for entry in jsonified:
	if entry.get('type') == 'PushEvent':
		push_event_ct+=1
	else:
		other_event_ct+=1 
print push_event_ct
print other_event_ct