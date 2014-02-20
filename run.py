from scraper.scraper import Scraper
import json

res = json.loads(results[0])
print json.dumps(res, sort_keys=False, indent=4, separators=(',', ': '))
