import sys
import json
import requests
from secrets import secrets


def getData(query, offset=0, page_size=100):
    url = "https://api.os.uk/search/names/v1/find"
    params = {'key': secrets['key'], 'query': query,
              'maxresults': page_size, 'offset': offset}

    response = requests.get(url, params=params)
    res = []
    more = False
    if response.status_code == 200:
        results = json.loads(response.content)
        total = results['header']['totalresults']

        for result in results['results']:
            entry = result['GAZETTEER_ENTRY']
            res.append(entry)
        if total > offset + page_size:
            more = True
        return (more, res)
    else:
        print(response.status_code)
        print(response.text)
        print(response.url)
        sys.exit(2)


def runQuery(query):
    data = []
    more = True
    offset = 0
    page_size = 100
    while more:
        more, res = getData(query, offset, page_size)
        data += res
        offset += page_size

    return data


# places = runQuery("Southampton")
# print(len(places))
# print(places[0])

places = runQuery("Glasgow")
print(len(places))
print(places[0])
