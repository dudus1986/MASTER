"""enable wifi skript"""

""" requests is the module that is for HTTPS requests using python"""
import requests

""" my org id is id is 454861 - network ID is L_659777345409787443 for Crewe """

url = "https://api.meraki.com/api/v0/networks/L_659777345409787443/ssids/5"

headers = {"X-Cisco-Meraki-API-Key": "3a18562c3c7888509be73b4ff6e46f53b24dbfa5"}

payload = {
    "name": "wow sid",
    "enabled": "false",
    "authMode":"ipsk-without-radius"
}

response = requests.request("PUT", url, data=payload, headers=headers)


print("\nAPI Response: \n{}".format(response.text))
print("\nStatus code: {}".format(response.status_code))