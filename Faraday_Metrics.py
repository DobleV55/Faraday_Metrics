import requests
import click
from bs4 import BeautifulSoup

def main():
    token = click.prompt('Access your Github token',type=str)
    print('')
    print('Stars')
    print('')
    get_stars()
    print('')
    print('Git Clone')
    print('')
    get_clone(token)
    print('')
    print('Visitors')
    print('')
    get_views(token)
    print('')
    print('Downloads')
    print('')
    download_count()
    print('')
    print('Pypi Stats')
    print('')
    pypi_stats()

def get_stars():
    repositories = ['faraday', 'faraday_plugins','faraday_agent_dispatcher','faraday_burp','faraday_zap']
    for repo in repositories:
        url = 'https://github.com/infobyte/'+repo
        print(repo)
        get = requests.get(url)
        soup = BeautifulSoup(get.content, 'html.parser')
        match = (soup.find('a', class_='social-count js-social-count'))
        matcha = match.attrs['aria-label']
        print(matcha)


def get_clone(token):
    user = 'DobleV55'
    response = requests.get('https://api.github.com/repos/infobyte/faraday/traffic/clones', auth=(user, token))
    json = response.json()

    clone_count = json['count']
    clone_unique = json['uniques']
    print('Git clones count: ',clone_count)
    print('Git clones unique: ',clone_unique)

def get_views(token):
    user = 'DobleV55'
    response1 = requests.get('https://api.github.com/repos/infobyte/faraday/traffic/views', auth=(user, token))
    json = response1.json()
    
    view_count = json['count']
    view_unique = json['uniques']
    print('View count: ', view_count)
    print('View unique: ', view_unique)

def download_count():
    url = 'https://api.github.com/repos/infobyte/faraday/releases'
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
            print(url)
            up_version = (url[54:])
            version = up_version.split('/')[0]
            print('Downloads: ', download_count)
        if downloads_per_asset != 0: 
            total_downloads = total_downloads + downloads_per_asset
            print('Downloads on version '+version+':',downloads_per_asset )
            print('')
    print('')
    print('Total Downloads for Faraday: ',total_downloads)

def pypi_stats():
    packages = ['faradaysec','faraday-plugins','faraday-agent-dispatcher']
    for package in packages:
        print('')
        url = 'https://pypistats.org/api/packages/'+package+'/recent'
        get = requests.get(url)
        json = get.json()
        package = json['package']
        data = json['data']
        last_day = data['last_day']
        last_week = data['last_week']
        last_month = data['last_month']
        print(package)
        print('Last Day: ', last_day)
        print('Last Week: ', last_week)
        print('Last Month: ', last_month)

if __name__ == "__main__":
    main()