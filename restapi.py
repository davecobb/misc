import requests

url="http://md5.jsontest.com/?text=dcobb"
t=requests.get(url,verify=False)
print(t.text)