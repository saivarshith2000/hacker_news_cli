import argparse
from datetime import datetime, timedelta

from . import scraper
from . import ui


def main():
    argParser = initArgParser()
    args = argParser.parse_args()
    # Obtain the args
    newsType = args.type
    pages = args.number
    proxy = args.proxy
    age = args.age
    args = argParser.parse_args()
    config = args.config

    # Validate and merge config data

    # Obtain the results based on request newsType
    if newsType == "news":
        results = scraper.getNews(pages)
    elif newsType == "latest":
        results = scraper.getLatest(pages)
    elif newsType == "past":
        # Use age passed in the args or default to 1
        if age != None:
            if age < 1 or age > 30:
                print(
                    "Invalid age argument. age must be greater than 1. Showing Front Page ..."
                )
                results = scraper.getNews(pages)
                return
            print("\nShowing Results from {} days ago".format(age), end="")
            results = scraper.getPast(datetime.now() - timedelta(age), pages)
        else:
            print("\nShowing Results from 1 day ago", end="")
            results = scraper.getPast(datetime.now() - timedelta(1), pages)

    # Display formatted results
    ui.printAllResults(results)
    exit()


def initArgParser():
    # Initialise the return the argParser
    parser = argparse.ArgumentParser(description="Hacker News Cli")
    parser.add_argument(
        "-number", type=int, help="Number of pages to display. Default = 1", default=1
    )
    parser.add_argument(
        "-proxy",
        type=str,
        help="Network Proxy. Default = Config Value or None",
        default=None,
    )
    parser.add_argument(
        "-type",
        type=str,
        help="Type of news ie, news, latest, past. Default = news",
        default="news",
    )
    parser.add_argument("-age", type=int, help="Age of results in DAYS")
    parser.add_argument(
        "-config", type=str, help="Path to Config. Default = ~/.hnews.ini"
    )
    return parser


if __name__ == "__main__":
    main()
