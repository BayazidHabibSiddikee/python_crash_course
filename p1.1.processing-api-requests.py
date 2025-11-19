import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept':'application/vnd.github.v3+json'}
try:
    r = requests.get(url,headers=headers)
    print(r.status_code)
except Exception as e:
    print('Invalid')

#Store the api in a variable
res = r.json()

#Result
print(res.keys())


print(f"Total repo{res['items']}")

#Explore information about repo
repo_dict = res['items']
print(f'Repository returned {len(repo_dict)}')

#examine the first repository
repo = repo_dict[0]
print(f'Keys {len(repo)}')

for a in sorted(repo.keys()):
    print(a)
