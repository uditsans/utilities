import json

f = open('keys.json', 'r')
a = dict(json.load(f))
f.close()

print(f"The username is {a['username']}")
print(f"The password is {a['password']}")