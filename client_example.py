import json
import requests

SERVER_URL = "http://127.0.0.1:5000"

evidence_payload = {
    "evidence_id": 1,
    "evidence_data": [
        {
            "login_name": "anecdotes - exercise",
            "role": "owner",
            "user_details": {
                "updated_at": "2021 - 07 - 26 T09: 41: 56 Z",
                "id": 120000,
                "email": "exercise @anecdotes.ai",
                "first_name": "anec",
                "last_name": "dotes"
            },
            "security": {
                "mfa_enabled": "True",
                "mfa_enforced": "True"
            }
        },
        {
            "login_name": "anecdotes - exercise",
            "role": "owner",
            "user_details": {
                "updated_at": "2021 - 07 - 26 T09: 41: 56 Z",
                "id": 120000,
                "email": "exercise @anecdotes.ai",
                "first_name": "anec",
                "last_name": "dotes"
            },
            "security": {
                "mfa_enabled": "True",
                "mfa_enforced": "True"
            }
        },
        {
            "login_name": "anecdotes - exercise",
            "role": "owner",
            "user_details": {
                "updated_at": "2021 - 07 - 26 T09: 41: 56 Z",
                "id": 120000,
                "email": "exercise @anecdotes.ai",
                "first_name": "anec",
                "last_name": "dotes"
            },
            "security": {
                "mfa_enabled": "True",
                "mfa_enforced": "True"
            }
        },
        {
            "login_name": "anecdotes - exercise",
            "role": "owner",
            "user_details": {
                "updated_at": "2021 - 07 - 26 T09: 41: 56 Z",
                "id": 120000,
                "email": "exercise @anecdotes.ai",
                "first_name": "anec",
                "last_name": "dotes"
            },
            "security": {
                "mfa_enabled": "True",
                "mfa_enforced": "True"
            }
        },
        {
            "login_name": "anecdotes - exercise",
            "role": "owner",
            "user_details": {
                "updated_at": "2021 - 07 - 26 T09: 41: 56 Z",
                "id": 120000,
                "email": "exercise @anecdotes.ai",
                "first_name": "anec",
                "last_name": "dotes"
            },
            "security": {
                "mfa_enabled": "True",
                "mfa_enforced": "True"
            }
        }
    ]
}

url = f"{SERVER_URL}/parse"
body = dict()
body["parsing_configuration"] = {
    "id": [["user_details", "id"]],
    "full name": [["user_details", "first_name"], ["user_details", "last_name"]],
    "email": [["user_details", "email"]],
    "updated_at": [["user_details", "updated_at"]],
    "MFA enabled": [["security", "mfa_enabled"]],
    "MFA enforced": [["security", "mfa_enforced"]]
}

body["payload"] = evidence_payload

response = requests.post(url=url.format(SERVER_URL),
                         json=body,
                         headers={"Content-Type": "application/json"})

print(json.dumps(json.loads(response.content), indent=4))