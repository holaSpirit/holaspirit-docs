import requests
import sys

# configuration
email = ''
password = ''

client_id = '54cb79d0279871e1248b4567_400tdzqbdcowsskk08gws0wkwogck00w084w4s8w8gok08s0o8'
client_secret = ''
# end of configuration

domain = 'https://app.holaspirit.com/';

# Request to receive the access token
r = requests.post(domain + "oauth/v2/token", {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'password',
    'username': email,
    'password': password
})

# Check that request succeeded
if not r.ok:
    print(r.status_code)
    print(r.content)
    sys.exit()

# Store the access token
json = r.json()
accessToken = json['access_token']

# Request other data on the API
# The same access_token can be used during 24 hours
r = requests.get(domain + "api/me", headers={
    'Authorization': 'Bearer '+accessToken
})

# Check that request succeeded
if not r.ok:
    print(r.status_code)
    print(r.content)
    sys.exit()

# Display the response
json = r.json()
print(json)
