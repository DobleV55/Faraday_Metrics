import os
from influxdb import InfluxDBClient
from Faraday_Metrics import *

token = (os.environ['GHTOKEN'])
user = (os.environ['GHUSER'])

repositories = ['faraday','faraday_plugins','faraday_agent_dispatcher','faraday_burp']

faraday = {}
faraday_plugins = {}
faraday_agent_dispatcher = {}
faraday_burp = {}

for repo in repositories:
    stars = get_stars(repo)
    clone = get_clone(user,repo,token)
    views = get_views(user,repo,token)
    if repo == 'faraday':
        downl = get_downl(repo)
        faraday['stars'] = stars
        faraday['clone'] = clone
        faraday['views'] = views
        faraday['downl'] = downl
    if repo == 'faraday_plugins':
        faraday_plugins['stars'] = stars
        faraday_plugins['clone'] = clone
        faraday_plugins['views'] = views
    if repo == 'faraday_agent_dispatcher':
        faraday_agent_dispatcher['clone'] = clone
        faraday_agent_dispatcher['stars'] = stars
        faraday_agent_dispatcher['views'] = views
    if repo == 'faraday_burp':
        faraday_burp['clone'] = clone
        faraday_burp['stars'] = stars
        faraday_burp['views'] = views
