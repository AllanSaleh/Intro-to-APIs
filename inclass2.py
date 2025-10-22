import requests

# Headers
# Headers: we store additional information about our request (date format, credentials)

def send_with_headers():

  url = "https://reqres.in/api/users"

  my_headers = {
    'x-api-key': 'reqres-free-v1',
    'Content-Type': "application/json",
    # 'Authorization': "#Token"
  }

  body = {
    "email": "allan@email.com",
    "first_name": "Allan",
    "last_name": "Ahmed",
    "avatar": "N/A"
  }

  response = requests.post(url, json=body, headers=my_headers)
  print(response.status_code)

  if response.status_code == 201:
    data = response.json()
    print(data)

send_with_headers()