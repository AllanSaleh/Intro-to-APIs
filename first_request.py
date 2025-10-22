import requests #Imports the request library that we installed, so that we can actually use it

def send_request():
  '''Making a request to the JSONPlaceholder API'''

  # Step 1: Define our URL and our endpoint (route)
  url = "https://jsonplaceholder.typicode.com/posts"

  # Step 2: Make the request which will return a response object
#          Http Method |
  response = requests.get(url)

  #Step 3: Check what we got back
  print("Status Code: ", response.status_code)
  # print("Raw response: ", response.text)

  #Step 4: Parse JSON data (make it something useful in Python)
  if response.status_code == 200:
    data = response.json() #Converts JSON into Python dictionary
    print(data[1])


send_request()