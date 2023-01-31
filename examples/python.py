import requests
import sys

# configuration
email = ''
password = ''

client_id = '54cb79d0279871e1248b4567_400tdzqbdcowsskk08gws0wkwogck00w084w4s8w8gok08s0o8'
client_secret = ''
# end of configuration

domain = 'https://app.holaspirit.com/'

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
currentOrganizationId = json['data']['settings']['currentOrganization']

# request all roles of the current organization and save them in a dictionary
offset = 0
limit = 100
total = 1000
dict = dict()
while (offset + limit < total):
    r = requests.get(domain + "api/organizations/" + currentOrganizationId + "/roles?from=" + str(offset) + "&limit=" + str(limit), headers={
        'Authorization': 'Bearer '+accessToken
    })
    offset += limit
    json = r.json()
    total = json['pagination']['totalItems']
    for role in json['data']:
        dict[role['id']] = {"name":role['name']}

print(dict)

# example of a PATCH
#r = requests.patch(
#    domain + '/api/organizations/'+currentOrganizationId+'/members/'+memberId,
#    headers={'Authorization': 'Bearer '+accessToken},
#    json={"phone":"+33 6 00 00 00 00"}
#)
