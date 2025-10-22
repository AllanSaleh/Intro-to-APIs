import requests

def get_random_dog():
    """
    Get a random dog picture and print it to the terminal
    
    API Endpoint: https://dog.ceo/api/breeds/image/random
    Look at the documentation to see the response format!
    """
    # 1. Make a GET request to the API
    url = "https://dog.ceo/api/breeds/image/random"
    # 2. Get the JSON response  
    response = requests.get(url)
    # 3. Print the image URL
    if response.status_code == 200:
        data = response.json()
        print("Random dog image:", data['message'])

# Test your function
get_random_dog()