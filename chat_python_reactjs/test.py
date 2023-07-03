import requests

base_url = 'http://localhost:8000'

# API endpoint: create-group
create_group_url = f'{base_url}/create-group/'
create_group_payload = {
    'name': 'Group Chat One',
    'members': [2, 3]
}

try:
    response = requests.post(create_group_url, json=create_group_payload)
    response_json = response.json()
    print(response_json)
except requests.exceptions.JSONDecodeError:
    print(response.content)