import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

requests.packages.urllib3.disable_warnings()

def main():
    token = get_auth_token()
    network_dev = get_network_devices(token)
    pprint(network_dev.json())

def get_auth_token():

    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    username = 'devnetuser'
    password = 'Cisco123!'
    response = requests.post(url, auth=HTTPBasicAuth(username, password))
    token = response.json()['Token']
    
    return token

def get_network_devices(token):
    url = 'https://sandboxdnac.cisco.com/api/v1/network-device'
    header = {'x-auth-token':token, 'content-type':'application/json'}
    query = {'managementIpAddress':'10.10.22.73'}
    response = requests.get(url, headers=header, params=query)
    return response
if __name__ == '__main__': main()

