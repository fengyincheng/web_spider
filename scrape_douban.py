import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
respond = requests.get("https://movie.douban.com/top250",headers= headers)
if respond.ok:
    print("拿下!")
else:
    print("fail......")

