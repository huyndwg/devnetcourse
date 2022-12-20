import json
import requests

baseURL = "https://api.meraki.com/api/v1"
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

def get_org():
    url_org = baseURL + "/organizations"
    headers = {
        "X-Cisco-Meraki-API-Key" : api_key,
        "Content-Type" : "application/json"
    }
    send_request = requests.get(url_org, headers=headers)
    # show_org = json.dumps(send_request.json(),indent=4)
    # print(show_org)
    id_org = send_request.json()[0]["id"]
    return id_org


def get_network(id_org):
    url_org = baseURL + "/organizations/" + str(id_org) + "/networks"
    headers = {
        "X-Cisco-Meraki-API-Key" : api_key,
        "Content-Type" : "application/json"
    }
    send_request = requests.get(url_org, headers=headers)
    # show_network = json.dumps(send_request.json(),indent=4)
    # print(show_network)
    networkID = send_request.json()[0]["id"]
    return networkID


def get_devices(networkId):
    url_device = baseURL + "/networks/"+ str(networkId) + "/devices"
    headers = {
        "X-Cisco-Meraki-API-Key" : api_key,
        "Content-Type" : "application/json"
    }
    send_request = requests.get(url_device, headers=headers)
    # show_devices = json.dumps(send_request.json(),indent=4)
    # print(show_devices)
    serialId = send_request.json()[0]["serial"]
    return serialId


def get_SSID_info(networkId, serialId):
    url_ssid_device = baseURL+"/networks/" + str(networkId) + "/devices/" + str(serialId)
    headers = {
        "X-Cisco-Meraki-API-Key": api_key,
        "Content-Type": "application/json"
    }
    send_request = requests.get(url_ssid_device, headers=headers)
    show_ssid_devices = json.dumps(send_request.json(),indent=4)
    print(show_ssid_devices)


if __name__ == "__main__":
    id_org = get_org()
    networkId = get_network(id_org=id_org)
    serialId = get_devices(networkId=networkId)
    get_SSID_info(networkId=networkId, serialId=serialId)