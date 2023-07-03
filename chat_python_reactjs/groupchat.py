import requests

base_url = 'http://localhost:8000'
group_id = '450041cb-923d-4d90-b929-caa5ab726f3e'
# Yêu cầu POST để gửi một tin nhắn mới tới một nhóm
send_message_url = f'{base_url}/send-message/{group_id}/'
send_message_payload = {
    'message': 'Banj ddang lam gif vay',
    'sender_id': 'a1f357bd-a734-484f-b5dd-aa1166b6ab2d'
}
response = requests.post(send_message_url, json=send_message_payload)
print(response.json())
