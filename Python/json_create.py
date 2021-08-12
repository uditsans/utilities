import json

a = {}
a['username'] = input('Enter Username: ')
a['password'] = input('Enter Password: ')

f = open('keys.json', 'w')
f.write(json.dumps(a))
f.close()
