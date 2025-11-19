from plotly.graph_objs import Bar,Layout
from plotly import offline 
import requests,sys

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
try:
    a = requests.get(url,headers=headers)
    #print(a.status_code())
except Exception as e:
    print(f'error')
    sys.exit()
    
data = a.json()#Turning json to python dictionary
#print(data)



repo_link , stars , labels =[],[],[]
repo = data['items']
for i in repo:
    repo_name = i['name']
    repo_url = i['html_url']
    repo_link.append(f"<a href='{repo_url}'>{repo_name}</a>") #creating link though 
    
    stars.append(i['stargazers_count'])
    owner = i['owner']['login']
    des = i['description']
    label = f'{owner}<br/>{des}'
    labels.append(label)
    
data = [{
    'type':'bar',
    'x':repo_link,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]

layout = {
    'title':'Most-Starred python project on Github',
    #'font':{'size':24},
    'xaxis':{   
        'title':'Repository',
     #   'font':{'size':24},
        'tickfont':{'size':14},
    },
    'yaxis':{   
        'title':'Stars',
      #  'font':{'size':24},
        'tickfont':{'size':14},
    },
}

offline.plot({'data':data,'layout':layout},filename='p1.2.visualise-repo.html')
