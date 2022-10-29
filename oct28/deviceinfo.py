from sdwan_lib import Sd_wan
from tabulate import tabulate


def main():
    # Get device info
    cookies = Sd_wan.get_cookies(end_point="/j_security_check", username="devnetuser", password="RG!_Yw919_83")
    token = Sd_wan.get_token(jsessionid=cookies)
    device = Sd_wan.get_device(end_point="/device", jsesssionid=cookies, token=token)
    # Format device info
    headers_table = ["Hostname", "Device", "UUID", "Status"]
    table_data = []
    for item in device["data"]:
        row = [item["host-name"], item["deviceId"], item["uuid"], item["status"]]
        row = [item["host-name"], item["deviceId"], item["uuid"], item["status"]]
        table_data.append(row)
    # Print device info
    table = tabulate(table_data, headers=headers_table, tablefmt="github")
    print(table)


if __name__ == "__main__":
    main()