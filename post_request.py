import requests
# POST requests: are requests to send information to our backend to be storied in our database

# How do we send that info?

# GET request: https://jsonplaceholder.typicode.com/posts

# POST request:
# url: https://jsonplaceholder.typicode.com/posts
# Body: {"Title": "My new post", "userID": 1} Information that we are attaching to the request

def create_new_post():
  '''Endpoint to send a POST request to the JSONPlaceholder API'''

  url = "https://jsonplaceholder.typicode.com/posts"

  # Create request body
  post_data = {
    "title": "My first post!",
    "body": "Super happy to be a new user on Fakebook",
    "userId": 1
  }

# Sending a post request
  response = requests.post(url, json=post_data)

  if response.status_code == 201: #Checking for a successful creation
    data = response.json()
    print(f"User id: {data["userId"]} has successfully posted, Title: {data['title']}")

create_new_post()
