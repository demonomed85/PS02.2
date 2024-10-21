import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'userId': 1
}
responce = requests.get(url, params=data)
print(responce.status_code)
print(responce.headers)
print(responce.text)
