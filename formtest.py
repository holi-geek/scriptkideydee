import requests

# URL of the login form
url = 'https://truehost.co.ke/cloud//index.php?rp=/login'

# Username and password to test
username = 'testuser'
password = 'testpassword'

# CSRF token value
csrf_token = 'dd'

# Create a session object to persist cookies across requests
session = requests.Session()

# Submit the login form with the username, password, and CSRF token
login_data = {
    'username': username,
    'password': password,
    'csrfmiddlewaretoken': csrf_token
}
response = session.post(url, data=login_data)

# Check if the login was successful
if 'Welcome' in response.text:
    print('Login successful')
else:
    print('Login failed')

