import requests

url = "https://steamcommunity.com/profiles/76561198231636540/inventory/json/730/2"

payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Cookie': 'steamLoginSecure=76561198231636540%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxRV8yMjhEQTgxQV8yMEY4RCIsICJzdWIiOiAiNzY1NjExOTgyMzE2MzY1NDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4NTgwOTg4OSwgIm5iZiI6IDE2NzcwODI4OTgsICJpYXQiOiAxNjg1NzIyODk4LCAianRpIjogIjBEMkFfMjJBMDFFOEJfQzA4NjUiLCAib2F0IjogMTY4NDg0OTkyOSwgInJ0X2V4cCI6IDE3MDI4MjQ5NzMsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxMDkuMjMxLjYyLjMxIiwgImlwX2NvbmZpcm1lciI6ICIxMDkuMjMxLjYyLjMxIiB9.oU4RYJSdw6B4beqUGopNapWp5wsQUWh4jLkmrlBjW9EBMCvyPVZXC6CCnaWA7AGAq8Y7n70xMAs9Ki5V5lUfAA;',
  'DNT': '1',
  'Pragma': 'no-cache',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'Referer': 'https://steamcommunity.com/profiles/76561198231636540/inventory/json/730/2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
