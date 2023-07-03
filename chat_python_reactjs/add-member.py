import requests

base_url = 'http://localhost:8000'

# API endpoint: add-member
group_id = 12
add_member_url = f'{base_url}/add-member/{group_id}/'
add_member_payload = {
    'member_id': 13
}

response = requests.post(add_member_url, json=add_member_payload)
print(response.json())