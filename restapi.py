import requests

# get MD5 and return hashed result
url="http://md5.jsontest.com/?text=dcobb"
t=requests.get(url,verify=False)
print(t.text)
