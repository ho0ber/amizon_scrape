from scraper.scraper import Scraper
import json

results = Scraper().scrape()
res = json.loads(results[0])
print json.dumps(res, sort_keys=False, indent=4, separators=(',', ': '))
