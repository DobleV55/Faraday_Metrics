from handshake import *

client = InfluxDBClient(host='localhost', port='8086')
client.switch_database('GRAFANA')

json = [
    {
        "measurement": "Faraday",
        "tags": {
        },
        "fields": {
            "Stars":faraday['stars'],
            "Clone": faraday['clone'],
            "Visitors":faraday['views'],
            "Downloads":faraday['downl']
                    },
           },
    {
        "measurement": "Faraday_Plugins",
        "tags": {
        },
        "fields": {
            "Stars":faraday_plugins['stars'],
            "Clone":faraday_plugins['clone'],
            "Visitors":faraday_plugins['views'],
                    },
           },
    {
        "measurement": "Faraday_Agent_Dispatcher",
        "tags": {
        },
        "fields": {
            "Stars":faraday_agent_dispatcher['stars'],
            "Clone": faraday_agent_dispatcher['clone'],
            "Visitors":faraday_agent_dispatcher['views'],
                    },
           },
    {
        "measurement": "Faraday_Burp",
        "tags": {
        },
        "fields": {
            "Stars":faraday_burp['stars'],
            "Clone": faraday_burp['clone'],
            "Visitors":faraday_burp['views'],
                    },
           },
    ]
    
client.write_points(json)