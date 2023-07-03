import requests
import json
base_url = 'http://localhost:8000'

create_group_url = f'{base_url}/create-group/'
create_group_payload = {
    'name': 'Chat id',
    'members': [1, 2, 3, "a1f357bd-a734-484f-b5dd-aa1166b6ab2d"]
}

response = requests.post(create_group_url, json=create_group_payload)
print(response.json())