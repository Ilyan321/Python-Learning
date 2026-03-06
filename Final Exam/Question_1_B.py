import requests
import time
url="https://zenquotes.io/api/random"
headers={"User-Agent": "Mogilla"}
for i in range(5):
    response=requests.get(url,headers=headers)

    if response.status_code== 200:
        data=response.json()
        quote=data[0]['q']
        author=data[0]['a']
        print(quote,"-",author)
        time.sleep(10)
    else:
        print("Cant fetch quotes.")
print("5 quotes generated. Leaving program now.")



