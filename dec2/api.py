import requests


access_token = "MmY0MGUwNzEtOTE3MS00MDRhLTkyYzEtYTI5NDZhNzRmZmM5YmExZDA2YWYtNjZk_P0A1_caac8e9f-ddc7-4e4f-ab82-d031172a892e"
base_url = "https://webexapis.com"
headers = {
    "Authorization" : f"Bearer {access_token}",
    "Content-Type" : "application/json"
}


def get_bot_id():
    url = f'{base_url}/people/me'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    return response.json()['id']


def get_message(messageId):
    url = f"{base_url}/v1/messages/{messageId}"

    response = requests.get(url=url, headers=headers)
    msg_text = response.json()['text']

    return msg_text


def post_message(roomId, text_msg):
    url = f"{base_url}/v1/messages/"

    body = {
        "roomId":roomId,
        "text" : text_msg
    }

    response = requests.post(url=url, headers=headers, json=body)
    # print(response.content)


if __name__ == "__main__":
    print(get_bot_id())