import requests

# Query Parameters

# Another way to send data info to our server

# example
# https://jsonplaceholder.typicode.com/posts?userId=1

# Query params come after '?'
# - organized in key value pairs: key=value
# - often used in filter, sorting, sending quick data

def query_params():
  '''Testing using query parameters, sending info through the url'''

  url = "https://jsonplaceholder.typicode.com/posts"

  my_params = {
    "userId": 1
  }

  response = requests.get(url, params = my_params)

  print(response.status_code)

  if response.status_code == 200:
    data = response.json()
    print("User1 post titles")
    for post in data:
      print("-", post["title"])

query_params()