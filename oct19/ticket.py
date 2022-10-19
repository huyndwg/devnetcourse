import requests
import json

base_url = "https://10.215.26.122/api/v1"

def ticket():
    url = base_url + '/ticket'
    header = {
        'Content-Type':'application/json'
    }
    body = {
        'username':'admin',
        "password":"vnpro@149"
    }
    json_body = json.dumps(body)
    
    response = requests.post(url=url, headers=header, data=json_body, verify=False)
    return response.json()['response']['serviceTicket']

def get_network_device():
    url = base_url + '/network-device'
    header = {
        'Content-Type':'application/json',
        'X-Auth-Token':ticket()
    }
    response = requests.get(url=url, headers=header, verify=False)
    data_dict = response.json()
    return json.dumps(data_dict, indent=4)

def main():
    print(ticket())
    print(get_network_device())

if __name__ == '__main__':
    main()