import requests

response = requests.get('https://www.google.com')
print(response.status_code) 
#print status code
# if status code is 200, ssl certificate is correctly installed