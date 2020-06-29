import requests
import click
from bs4 import BeautifulSoup

def get_stars(repo):
    url = 'https://github.com/infobyte/'+repo
    get = requests.get(url)
    soup = BeautifulSoup(get.content, 'html.parser')
    match = (soup.find('a', class_='social-count js-social-count'))
    matcha = match.attrs['aria-label']
    stars = int(matcha.split('u')[0])
    return stars

def get_clone(user, repo, token):
    response = requests.get('https://api.github.com/repos/infobyte/'+repo+'/traffic/clones', auth=(user, token))
    json = response.json()
    clone_count = json['count']
    clone_unique = json['uniques']
    clone = clone_count+clone_unique #Done
    return clone

def get_views(user, repo, token):
    response1 = requests.get('https://api.github.com/repos/infobyte/'+repo+'/traffic/views', auth=(user, token))
    json = response1.json()
    view_count = json['count']
    view_unique = json['uniques']
    view = view_unique+view_count
    return view

def get_downl(repo):
    url = 'https://api.github.com/repos/infobyte/'+repo+'/releases'
    get = requests.get(url)
    dicts = get.json()
    total_downloads = 0    
    for diction in dicts:
        assets = (diction['assets'])
        downloads_per_asset = 0
        for item in assets:
            download_count = item['download_count']
            downloads_per_asset = downloads_per_asset + download_count
            asset_name = item['name']
            url = item['browser_download_url']
            up_version = (url[54:])
            version = up_version.split('/')[0] #FARADAY VERSION
            asset_count = download_count #asset count
        if downloads_per_asset != 0: 
            total_downloads = total_downloads + downloads_per_asset
            version_count = downloads_per_asset #version count        
    total_count = total_downloads #total count
    return total_count


def pypi_stats(repo):
    url = 'https://pypistats.org/api/packages/'+repo+'/recent'
    get = requests.get(url)
    json = get.json()
    package = json['package']
    data = json['data']
    last_day = data['last_day']
    last_week = data['last_week']
    last_month = data['last_month']
    print(repo)
    print('Last Day: ', last_day)
    print('Last Week: ', last_week)
    print('Last Month: ', last_month)
