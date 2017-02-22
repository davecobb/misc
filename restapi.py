import requests

url="http://date.jsontest.com/"
t=requests.get(url,verify=False)
print(t.text)