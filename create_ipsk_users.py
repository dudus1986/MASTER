"""create 3 wifi users"""

""" requests is the module that is for HTTPS requests using python"""
import requests

""" my org id is id is 454861 - network ID is L_659777345409787443 for Crewe """

"""need to use V1 for IPSK"""





url = "https://api.meraki.com/api/v1/networks/L_659777345409787443/wireless/ssids/5/identityPsks

headers = {"X-Cisco-Meraki-API-Key": "3a18562c3c7888509be73b4ff6e46f53b24dbfa5"}


response = requests.request("GET", url, headers=headers)


print("\nAPI Response: \n{}".format(response.text))
print("\nStatus code: {}".format(response.status_code))