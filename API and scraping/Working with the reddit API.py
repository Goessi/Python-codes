## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top",headers = headers,params=params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top["data"]['children']
post = 0
name = ""
for d in python_top_articles:
    data = d['data']
    if data['ups'] > post:
        post = data['ups']
        name = data['id']
most_upvoted = name


## 4. Getting Post Comments ##

response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u",headers=headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]['data']['children']
id_c = 0
ups = 0
for ch in comments_list:
    c = ch['data']
    if c['ups'] > ups:
        ups = c['ups']
        id_c = c['id']
most_upvoted_comment = id_c
    

## 6. Upvoting a Comment ##

params = {'dir':1,'id':'d16y4ry'}
response = requests.post("https://oauth.reddit.com/api/vote",headers=headers,json=params)
status = response.status_code  