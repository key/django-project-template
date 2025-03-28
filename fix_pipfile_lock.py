import json

with open('Pipfile.lock', 'r') as f:
    data = json.load(f)

if 'backports.zoneinfo' in data['default']:
    del data['default']['backports.zoneinfo']
if 'backports.zoneinfo' in data['develop']:
    del data['develop']['backports.zoneinfo']

with open('Pipfile.lock', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

print("Successfully removed backports.zoneinfo from Pipfile.lock")
