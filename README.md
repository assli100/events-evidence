# Events Evidence Service

## Prerequisites
- Python 3.9
## Installation
```bash
pip install -r requirements.txt
```

## Run the service
```bash
python src\app.py
```

## Test with a client
You can use the client_example.py script to feed the service.
The script already has some data to use.

```bash
python client_example.py
```

## How service works
The service gets from client evidence request and a parsing configuration. \
with the parsing configuration, the service know which data to extract from evidence and generates table-structured JSON.

### How to create a parser
parser configuration is a json based structure which its keys are the table headers and its values are the key path to the value to extract from the evidence
####example
- parser:
```json
{
    "id": [["user_details", "id"]],
    "full name": [["user_details", "first_name"], ["user_details", "last_name"]],
    "email": [["user_details", "email"]],
    "updated_at": [["user_details", "updated_at"]],
    "MFA enabled": [["security", "mfa_enabled"]],
    "MFA enforced": [["security", "mfa_enforced"]]
}
```
- evidence:
```json
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
```
you can use multiple keys in cases you need to union more that one value, as in ```full name``` attribute