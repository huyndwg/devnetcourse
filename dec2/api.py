from flask import request

access_token = "MmY0MGUwNzEtOTE3MS00MDRhLTkyYzEtYTI5NDZhNzRmZmM5YmExZDA2YWYtNjZk_P0A1_caac8e9f-ddc7-4e4f-ab82-d031172a892e"

base_url = "https://webexapis.com"

message_id = ""

headers = {
    "Authorization" : f"Bearer {access_token}",
    "Content-Type" : "application/json"
}



def get_messages():
    url = f"{base_url}/v1/messages/{message_id}"