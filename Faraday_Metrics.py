import requests
from bs4 import BeautifulSoup


# Get Views
# https://api.github.com/repos/infobyte/faraday_burp/traffic/views

## Get Clones
## https://api.github.com/repos/infobyte/faraday_burp/traffic/clones

### Get Pypi Stats
### https://pypistats.org/

def main():
    get_stars()
    download_count()

def get_stars():
    repos = ['https://github.com/infobyte/faraday/','https://github.com/infobyte/faraday_plugins','https://github.com/infobyte/faraday_agent_dispatcher','https://github.com/infobyte/faraday_burp','https://github.com/infobyte/faraday_zap']
    for repo in repos:
        print(repo)
        get = requests.get(repo)
        soup = BeautifulSoup(get.content, 'html.parser')
        match = (soup.find('a', class_='social-count js-social-count'))
        matcha = match.attrs['aria-label']
        print(matcha)


def download_count():
    url = 'https://api.github.com/repos/infobyte/faraday/releases'
    get = requests.get(url)
    dicts = get.json()
    total_downloads = 0    
    for diction in dicts:
        assets = (diction['assets'])
        print('---')
        downloads_per_asset = 0
        for item in assets:
            downloads_per_asset = downloads_per_asset + item['download_count']
            print(item['name'])
            url = item['browser_download_url']
            print(url)
            up_version = (url[54:])
            version = ''
            for letter in up_version: 
                version = version + letter
                if letter == '/':
                    break
            print('Downloads: '+str(item['download_count']))
        if downloads_per_asset != 0: 
            total_downloads = total_downloads + downloads_per_asset
        print('Downloads on version '+version+':',downloads_per_asset )

    print('Total Downloads: ',total_downloads)

if __name__ == "__main__":
    main()