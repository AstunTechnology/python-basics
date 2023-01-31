# Fetching Data from the Internet

## The Requests Module

[Requests](https://pypi.org/project/requests/) is an elegant and simple HTTP library for Python, built for 
human beings. It handles all sorts of internet requests in a user friendly and pythonic way. 

~~~py
import requests

r = requests.get("https://developer.ordnancesurvey.co.uk/")
print("status ",r.status_code)
print("content-type",r.headers['content-type'])
print("encoding",r.encoding)
print(r.text[:1000])
~~~

Generates this output:

~~~txt
D:\PhotonUser\My Files\Home Folder>python request.py
status  200
content-type text/html; charset=utf-8
encoding utf-8
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><script 
  type="text/javascript">(window.NREUM||(NREUM={})).init={ajax:{deny_list:["bam.nr-data.net"]}};(window.NREUM||(NREUM={})).loader_config={licenseKey:"5c41040092",applicationID:"190555206"};;(()=>{var 
  __webpack_modules__={507:(__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{"use 
  strict";function detectPolyfillFeatures(){const featureStatus={};return 
  checkAndAddFeature("Promise","PROMISE"),checkAndAddFeature("Array.prototype.includes","ARRAY_INCLUDES"),checkAndAddFeature("Object.assign","OBJECT_ASSIGN"),checkAndAddFeature("Object.entries","OBJECT_ENTRIES"),featureStatus;function 
  checkAndAddFeature(funcString,featName){try{let 
  func=eval("self."+funcString);-1!==func.toString().indexOf("[native 
  code]")?featureStatus[featName]=Status.NATIVE:featureStatus[featName]=Status.CHANGED}catch{featureStatus[featName]=Status.UNAVAIL}}}__webpack_re
~~~

## Making a Request

A simple web request is made using the `get` method which takes (at its simplest) a single URL string. This 
gives a `response` object (`r` in the example above) which contains all the information we need to use the web 
page. If you want to make a POST request to the server you use the `post` method again with a URL string, and 
usually the `data` parameter set to a dict of data for the request. All the other HTTP methods are implemented 
in the same way.

~~~py
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.head('https://httpbin.org/get')
~~~

### Status Codes

As we saw in the first example the response object includes a `status_code` that tells you (and your program) 
whether the request you sent worked or not and if not why not. 

The [status code will be in one of 5 groups](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) 
indicated by the first number of the code:

+ `1xx` informational response – the request was received, continuing process
+ `2xx` successful – the request was successfully received, understood, and accepted
+ `3xx` redirection – further action needs to be taken in order to complete the request
+ `4xx` client error – the request contains bad syntax or cannot be fulfilled
+ `5xx` server error – the server failed to fulfil an apparently valid request

#### `1xx` - Informational Responses

These codes are usually handled internally by web clients and are sent by the web server to provide some 
information. You usually don't need to worry about these in your code.

#### `2xx` - Successful Responses

The most common success response is `200` and this is what we test for most often, there are other responses 
such as `201 Created` and `202 Accepted` that can occur when you are working with REST APIs.

#### `3xx` - Redirection Responses

These are used by a server to tell the client that the page it asked for has moved for some reason, usually 
these responses will be handled by the client library. `304 Not Modified` can be a useful response to check 
for as it means that you don't need to download and process the content again as it is unchanged since the 
last time you fetched it.

#### `4xx` - Client Errors

The most common response in this group is `404 Not Found` when the page you requested in missing (this is 
usually due to a typo in your request, but it can be due to pages moving without a redirect being set). Other 
common errors are `401 Unathorised` and `403 Forbiden` which usually indicate an authorisation problem.

#### `5xx` - Server Errors

Any response in the `500` group indicates an issue with the web server, commonly this is a generic `500 
Internal Server` response, there is little you can do (unless its your server) but wait and try again.

### Adding Parameters to the Request

You often want to send data to the web server as key value pairs (KVP) - if we were doing this by hand we 
would type a `?` followed by the key name and value e.g `http://httpbin.org/get?key=val`. The requests library 
allows you to handle KVP by passing in a dict of the data values.

~~~txt
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)
>>> print(r.url)
https://httpbin.org/get?key2=value2&key1=value1
~~~

To learn more about Requests consult it's [fantastic 
documentation](https://requests.readthedocs.io/en/latest/).

## Requesting Data from the OS Download Service

To fetch data from the [Ordnance Survey Data Hub](https://osdatahub.os.uk/) you will first need to 
[register](https://osdatahub.os.uk/plans) (the free plan will be fine for this course) or 
[login](https://osdatahub.b2clogin.com/osdatahub.onmicrosoft.com/oauth2/v2.0/authorize?p=b2c_1a_prodsignuporsignin&redirect_uri=https%3A%2F%2Fosdatahub.os.uk%2Fapi%2Fauth%2FsignedIn&response_type=code&response_mode=form_post&client_id=427122a0-e325-4e6d-b1ac-841a0afb58b9&state=CUSTOMtVIIaTKmD076HheCLlHtL10-4m8UYNpy%2Fplans&nonce=LQPbw-cFg72KL4BhiXfF_-4XZaXFD6R-&scope=openid&x-client-SKU=passport-azure-ad&x-client-Ver=4.3.2) 
if you already have an account.

we can then go to the [APIs](https://osdatahub.os.uk/products) page to see the available APIs, for this 
exercise we will be using the OS Names API which allows us to find and verify postcodes, populated places, 
road names and much more. 

1. Right click this [link](https://osdatahub.os.uk/) and open the OS Data Hub in a new tab.
2. Click "API Dashboard" in the navigation menu.
3. Click "APIs" in the secondary navigation menu.
4. Click "Add to API project" next to the OS Names API.
5. If you already have a project you may choose to add the OS Names API into that project, or alternatively 
   Select "Add to NEW PROJECT".
6. The next screen will contain the Project API Key and the API Endpoint address (API URL).
7. You can return to this screen by clicking "My projects" at any point in the future if you need to copy your 
   API key or the API address, or if you need to regenerate your API Key.
8. Keep this page open as you'll need the key when you apply the OS Names API service in your web-based 
   application.

We'll now create a file `secrets.py` to hold our secret codes - 

~~~py
secrets = {'key':'Your project API Key',
           'secret':'Your project API Secret'}
~~~

It's important in a real project that you don't include this file in a your public code repository. Now, when 
we write code to access the API we can simply start our program with:

~~~py
from secrets import secrets

~~~

and then any time we need to refer to say the key we can use `secrets['key']` and it will be automatically 
filled in for us. If we pass our code to someone else all they need is to generate their own key and secrets 
file and the program will work for them too.

From the projects page we can also note the API endpoint address 
`https://api.os.uk/search/names/v1/{path}?key=`, to find out what the "path" should be we can look at the code 
examples (in javascript) or read the [technical 
docs](https://osdatahub.os.uk/docs/names/technicalSpecification). For a `query` seems that the simplest 
request must contain a `query` and a `key` parameter, and the request can locate a feature using just its 
name. 

So to test this out type (or paste) in this code:

~~~py
import json
import requests
from secrets import secrets

url = "https://api.os.uk/search/names/v1/find"
response = requests.get(url, params={'key':secrets['key'], 'query':'Southampton'})
print(response.url)
if response.status_code == 200:
  results = json.loads(response.content)
  print("---" * 10)
  for result in results['results']:
    entry = result['GAZETTEER_ENTRY']
    print(f"{entry['NAME1']}\t{entry['TYPE']}\t{entry['LOCAL_TYPE']}")
    print(f"\t({entry['GEOMETRY_X']},{entry['GEOMETRY_Y']})")
else:
  print(response.status_code)
  print(response.text)
~~~

And if all is well you should see:

~~~txt
D:\PhotonUser\My Files\Home Folder>python names.py
https://api.os.uk/search/names/v1/find?key=xxxxxxxxxxxx&query=Southampton
------------------------------
Southampton     populatedPlace  City
        (441982.0,111882.0)
Southampton Street      transportNetwork        Named Road
        (441929.0,112804.0)
Faculty of Medicine     other   Higher or University Education
        (439859.0,114981.0)
Gateley Hall    other   Higher or University Education
        (441584.0,113089.0)
Southampton Central     transportNetwork        Railway Station
        (441285.0,112167.0)
Southampton City College        other   Further Education
        (442717.0,111689.0)
Southampton Coach Station       transportNetwork        Coach Station
        (441638.0,112001.0)
Southampton Docks       transportNetwork        Port Consisting of Docks and Nautical Berthing
        (438354.0,112348.0)
Southampton Docks       transportNetwork        Port Consisting of Docks and Nautical Berthing
        (442531.0,110125.0)
Southampton Ferry Terminal      transportNetwork        Vehicular Ferry Terminal
        (441901.0,110933.0)
Southampton General Hospital    other   Hospital
        (439792.0,114941.0)
~~~

Note how I imported the `json` module that can read a string full of JSON data and parse it to a python `dict` 
or `list` depending on the type of JSON. 

If you want to see the raw JSON (which is how I worked out which fields I wanted), take the URL printed out by 
your program and paster it into Chrome (or other browser), you should get a page like this back:

~~~js
{
  "header" : {
    "uri" : "https://api.os.uk/search/names/v1/find?query=Southampton",
    "query" : "Southampton",
    "format" : "JSON",
    "maxresults" : 100,
    "offset" : 0,
    "totalresults" : 5264
  },
  "results" : [ {
    "GAZETTEER_ENTRY" : {
      "ID" : "osgb4000000074564709",
      "NAMES_URI" : "http://data.ordnancesurvey.co.uk/id/4000000074564709",
      "NAME1" : "Southampton",
      "TYPE" : "populatedPlace",
      "LOCAL_TYPE" : "City",
      "GEOMETRY_X" : 441982.0,
      "GEOMETRY_Y" : 111882.0,
      "MOST_DETAIL_VIEW_RES" : 73000,
      "LEAST_DETAIL_VIEW_RES" : 9000000,
      "MBR_XMIN" : 436729.0,
      "MBR_YMIN" : 109122.0,
      "MBR_XMAX" : 447910.0,
      "MBR_YMAX" : 117588.0,
      "POSTCODE_DISTRICT" : "SO14",
      "POSTCODE_DISTRICT_URI" : "http://data.ordnancesurvey.co.uk/id/postcodedistrict/SO14",
      "COUNTY_UNITARY" : "City of Southampton",
      "COUNTY_UNITARY_URI" : "http://data.ordnancesurvey.co.uk/id/7000000000037256",
      "COUNTY_UNITARY_TYPE" : "http://data.ordnancesurvey.co.uk/ontology/admingeo/UnitaryAuthority",
      "REGION" : "South East",
      "REGION_URI" : "http://data.ordnancesurvey.co.uk/id/7000000000041421",
      "COUNTRY" : "England",
      "COUNTRY_URI" : "http://data.ordnancesurvey.co.uk/id/country/england",
      "SAME_AS_GEONAMES" : "http://sws.geonames.org/2637487"
    }
  }, {
  ....
  }
~~~

For some reason all the field names are in capitals, there is a header that mostly tells us things we already 
know but does usefully tell us the total number of results. Then there is a key `results` that's value is a 
`list` of `dicts` each containing a single key ('GAZETTEER_ENTRY') which has a `dict` value that has actual 
results in it. So in our program we need to look at each object in the `results` array (`for result in 
results['results']:`) and then we need to extract the `GAZETTEER_ENTRY` from that `dict` (`entry = 
result['GAZETTEER_ENTRY']`)and then ask for individual fields from that `dict` (`entry['NAME1']`). Anything 
that was in the JSON in quotes will be a string, other values will be integers or floats depending on the 
presence or absence of a `.` in the digits. 

From the technical specification we can also see that we can restrict the number of results by adding 
`maxresults` and a number between 1 and 100, if we want to see later records then we can add an `offset` (100 
in most cases) to allow us to page through the results.

~~~py
import sys
import json
import requests
from secrets import secrets

def getData(query, offset=0, page_size=100):
    url = "https://api.os.uk/search/names/v1/find"
    response = requests.get(url, params={'key':secrets['key'], 'query':query,
        'maxresults':page_size, 'offset':offset})
    
    
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
    
places = runQuery("Southampton")
print (len(places))
print (places[0])
~~~

### Exercise - Filter by Local Type

The request can take an optional query parameter (`fq`) that allows you to specify a local type (or a bounding 
box). Take the previous program and modify it to limit the results returned by 

1. a single optional type and 
2. for bonus marks a list of local types (`&fq=LOCAL_TYPE:City LOCAL_TYPE:Bay&key=..`) and
3. finally think about how to implement limiting by `type` rather than `local_type` so you could ask for only 
   `populatedPlace`s instead of having to put each one in one at a time.
