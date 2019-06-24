# **Hacker News Cli**

#### A Simple command line tool written in python to browse Hacker news.

## **Introduction**
>Hacker News is a social news website focusing on computer science and entrepreneurship.  

hacker_news_cli is a command line tool which fetches and displays results from Hackernews website.
You can browse latest, top and past articles from the command line itself. 

## **Installation**
hacker_news_cli is written in python and can be installed with pip.  
**This program only supports python3**  
`pip3 install hacker_news_cli`  
You can also download source and try  
`python3 -m hnews`

## **Usage**
The tool can be run from the terminal using the hnews command.  
You can pass in various arguments to browse different parts of the Hackernews website.  
The tool supports the following arguments:  
* type - Type of news to fetch. Options are news, latest, past. Default is news
* number - number of pages to fetch. Each pages contains 30 articles. Default is 1
* age - age of the pages to fetch. It only works is 'past' flat is passed. 
* proxy - network proxy if you are using a proxy server. 
* config - config file containing your defaults. Default location is ~/.hnews.ini. More about config later

## **Config**
If you do not like the defaults, you can create a configuration file and the tool used that config  
for fetching data. Note that **config options are overriden** if you pass in arguments.  
number, type and proxy arguments are configurable ie., if you need to always pass any of these arguments (For example, proxy) you can just put it in the config and it is used as default

## **Example**
