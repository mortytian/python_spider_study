import requests

url = 'https://morvanzhou.github.io/static/files/Reinforcement_learning_An_introduction.pdf'
headers = {'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
}
response = requests.get(url, headers = headers)
print(response.status_code)
content = response.text
if response.status_code == 200:
    with open('rl.pdf', 'w') as w:
        w.write(content)

