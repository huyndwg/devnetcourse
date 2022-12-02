import requests

access_token = "MmY0MGUwNzEtOTE3MS00MDRhLTkyYzEtYTI5NDZhNzRmZmM5YmExZDA2YWYtNjZk_P0A1_caac8e9f-ddc7-4e4f-ab82-d031172a892e"

base_url = "https://webexapis.com"

message_id = ""

headers = {
    "Authorization" : f"Bearer {access_token}",
    "Content-Type" : "application/json"
}



def get_messages(messageId):
    url = f"{base_url}/v1/messages/{message_id}"

    response = requests.get(url=url, headers=headers)

    return response

def post_messages(roomId, text_msg):
    url = f"{base_url}/v1/messages/"

    body = {
        "roomId":roomId,
        "text" : text_msg
    }

    response = requests.post(url=url, headers=headers, json=body)

    print(response.status_code)

if __name__ == "__main__":
    print(get_messages(messageId=message_id))