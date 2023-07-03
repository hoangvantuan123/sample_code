import requests
import json
base_url = 'http://localhost:8000'

create_group_url = f'{base_url}/create-group/'
create_group_payload = {
    'name': 'Chat Base Group',
    'members': ["a1f357bd-a734-484f-b5dd-aa1166b6ab2d", "f8ffaadf-ff3f-4c3e-a0b4-1d730f7f37c0"]
}

response = requests.post(create_group_url, json=create_group_payload)
print(response.json())