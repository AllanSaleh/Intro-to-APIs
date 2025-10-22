# Lesson 6: API Fundamentals - Student Assignments

## Assignment Overview

Complete these assignments to master API integration with Python. Each assignment builds on the previous one, so work through them in order.

---

## Assignment 1: Get a Random Dog Picture 🐕

### Step 1: Look at the Documentation
Visit: **https://dog.ceo/dog-api/**

Find the endpoint for getting a random dog image.

### Step 2: Complete the Function
```python
import requests

def get_random_dog():
    """
    Get a random dog picture and print it to the terminal
    
    API Endpoint: https://dog.ceo/api/breeds/image/random
    Look at the documentation to see the response format!
    """
    # YOUR CODE HERE
    # 1. Make a GET request to the API
    # 2. Get the JSON response  
    # 3. Print the image URL
    pass

# Test your function
get_random_dog()
```

### Expected Output:
```
Random dog image: https://images.dog.ceo/breeds/hound-english/n02089973_612.jpg
```

---

## Assignment 2: Create a New User 👤

### Step 1: Look at the Documentation
Visit: **https://reqres.in/**

Find the endpoint for creating a new user (hint: look for POST /api/users).

### Step 2: Complete the Function
```python
import requests

def create_new_user():
    """
    Create a new user and print the response to the terminal
    
    API Endpoint: https://reqres.in/api/users
    Method: POST
    
    Look at the documentation to see what data you need to send!
    """
    # YOUR CODE HERE
    # 1. Set up the data you want to send (name, job)
    # 2. Make a POST request with json=your_data
    # 3. Get the JSON response
    # 4. Print the created user's ID, name, and createdAt timestamp
    pass

# Test your function
create_new_user()
```

### Expected Output:
```
User created successfully!
New user ID: 493
Name: John Doe
Job: Software Developer
Created at: 2024-01-15T10:30:45.123Z
```

---