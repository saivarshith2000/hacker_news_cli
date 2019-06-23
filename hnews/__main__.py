import argparse
import scraper
from ui import printAllResults

argParser = argparse.ArgumentParser(description="Hacker News Cli")
argParser.add_argument(
    "-number", type=int, help="Number of pages to display. Default = 1",
    default=1
)
argParser.add_argument(
    "-proxy",
    type=str,
    help="Network Proxy. Default = Config Value or None",
    default=None,
)
argParser.add_argument(
    "-type",
    type=str,
    help="Type of news ie, news, latest, past. Default = news",
    default="news",
)
argParser.add_argument("-age", type=int, help="Age of results in DAYS")
argParser.add_argument(
    "-date", type=str, help="Date of the results required in DD/MM/YYYY Format"
)

# Obtain the args
args = argParser.parse_args()
newsType = args.type
pages = args.number
proxy = args.proxy
age = args.age
date = args.date

# Obtain the results based on request newsType
if newsType == 'news':
    results = scraper.getNews(pages)
elif newsType == 'latest':
    results = scraper.getLatest(pages)

# Display formatted results
printAllResults(results)
exit()
