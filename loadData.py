#!/usr/bin/env python3

import json
import pysolr
import requests
# solr = pysolr.Solr("https://localhost:8983/solr/")

with open('wikipedia-movie-data/movies.json', 'r') as f:
    jd = f.read()
    x = json.loads(jd)

solr = pysolr.Solr('http://localhost:8983/solr/my_core/', timeout=10)
print(solr.ping())


solr.add(x)

solr.commit()


print("Searching for Buffalo movies")
r = requests.get("http://localhost:8983/solr/my_core/query?q=title:*buffalo*&q.op=OR&indent=true&rows=20")
res = r.json()


for rx in res['response']['docs']:
    print(f"{rx['title']} - {rx['year']}")
