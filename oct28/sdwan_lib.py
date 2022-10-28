import requests


base_url = "https://sandbox-sdwan-2.cisco.com/dataservice"


class Sd_wan():
    def __init__(self):
        pass

    def get_cookies(end_point : str, username : str, password : str):
        url = base_url + end_point
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        body = {
            "j_username" : username,
            "j_password" : password
        }
        response = requests.post(url=url, headers=headers, data=body)
        headers_split = response.headers["set-cookie"].split(";")
        # jsessionid_pre = headers_split[0].split("=")
        # jsessionid = jsessionid_pre[1]
        return headers_split[0]

    def get_token(jsessionid : str):
        url = f"{base_url}/client/token"
        headers = {
            "Cookie" : jsessionid
        }
        response = requests.get(url=url, headers=headers)
        return response.text

    def get_device(end_point : str, jsesssionid : str, token : str):
        url = base_url + end_point
        headers = {
            "Cookie" : jsesssionid,
            "X-XSRF-TOKEN" : token
        }
        response = requests.get(url=url, headers=headers)
        return response.json


def main():
    cookies = Sd_wan.get_cookies(end_point="/j_sercurity_check", username="devnetuser", password="RG!_Yw919_83")
    print(cookies)
    token = Sd_wan.get_token(jsessionid=cookies)
    print(token)
    # device = Sd_wan.get_device(end_point="", jsesssionid=cookies, token=token)
    # print(device)

if __name__ == "__main__":
    main()
