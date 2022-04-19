# Events Evidence Service
A simple service that generate table from a given data.

**My notes can be found in ```exercise_notes``` file
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
## Service api specifications
- Protocol: ```HTTP```, Port: ```5000```
- Paths:
    - /parse
        - Desciption: "Generates a table of evidence data using a given parsing_configuration"
        - Method: ```POST```
        - Request:
            - headers:
                - Content-type: ```application/json```
            - body:
                ```json
                {
                  "parsing_configuration": <json object>,
                  "payload": {"evidence_id": <number>, "evidence_data": <list of json objects>}
                }
                ```
        - Response:
            - headers:
                - Content-type: ```application/json```
            - body:
                ```json
                {
                    "evidence_id": <number>,
                    "headers": <list of strings>,
                    "rows": <list of objects>
                }
                ```
        - ```parsing_configuration```
            - Description: Is a \<key\>:\<value\> based object that defines the table.
                - \<key\> : column name of the resulting table
                - \<value\>: defines the keys path of the value that we want to extract from evidence. you can use single list to get single value of multiple lists to get multiple value seperated by space.
            - Example:
                - single value extraction:
                    ```json
                    "id": [["user_details", "id"]]
                    ```
                - multiple value extraction:
                    ```json
                    "full name": [["user_details", "first_name"], ["user_details", "last_name"]]
                    ```
                
### Example
For evidence with the following data:
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
and with the following parsing configuration:
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
the service will result this response:
```json
{
    "MFA enabled": "True",
    "MFA enforced": "True",
    "email": "exercise @anecdotes.ai",
    "full name": "anec dotes",
    "id": 120000,
    "updated_at": "2021 - 07 - 26 T09: 41: 56 Z"
}
```
