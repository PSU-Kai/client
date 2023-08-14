import requests

# The URL of the server to send the POST request to
SERVER_URL = 'http://131.252.223.181:8080'

# Data to be sent in the POST request
data_to_send = "Hello, server! This is a POST request from the client."

try:
    # Send a POST request to the server
    response = requests.post(SERVER_URL, data=data_to_send)
    
    # Print the response status code and content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print("An error occurred:", e)
