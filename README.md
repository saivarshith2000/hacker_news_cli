# **Py Hacker News**

#### A Simple command line tool written in python to browse Hacker news.

## **Introduction**
>Hacker News is a social news website focusing on computer science and entrepreneurship.  

py_hacker_news is a command line tool which fetches and displays results from Hackernews website.
You can browse latest, top and past articles from the command line itself. 

## **Installation**
py_hacker_news is written in python and can be installed with pip.  
**This program only supports python3**  
`pip3 install py_hacker_news --user`  
You need to make sure that `~/.local/bin` is in your PATH variable.  
To add this to the PATH try `export PATH=$PATH:~/.local/bin`  
  
You can also download source and try  
`pip install -r requirements.txt`  
`python3 -m hnews`

## **Usage**
The tool can be run from the terminal using the `hnews` command.  
You can pass in various arguments to browse different parts of the Hackernews website.  
The tool supports the following arguments:  
* type - Type of news to fetch. Options are news, latest, past. Default is news
* number - number of pages to fetch. Each pages contains 30 articles. Default is 1
* age - age of the pages to fetch. It only works is 'past' flat is passed. 
* proxy - network proxy if you are using a proxy server. 


## **Example**
`hnews` - displays 30 popular articles from hackernews  
`hnews -n 5` - displays 150 (30 * 5) popular articles from hackernews  
`hnews -t latest` - displays 30 newest articles from hackernews  
`hnews -t past -a 20 -n 2` - displays  60 (30 * 2) articles that were on front page 20 days ago from hackernews
`hnews -p https://proxy_address:port` - uses this proxy to connect to fetch articles

## **Proxy**
The tool automatically used proxy from environment variables if no proxy is provided in args. If   
a proxy flag is passed, that value is used instead. To set proxy environment variable:  
**On Linux**  
`export http_proxy=http://user:password@proxy.domain.com:port`  
`export https_proxy=http://user:password@proxy.domain.com:port`  
`export ftp_proxy=http://user:password@proxy.domain.com:port`  
**On Windows**  
`set http_proxy=http://user:password@proxy.domain.com:port`  
`set https_proxy=http://user:password@proxy.domain.com:port`  
  
## **Help**
In case of any trouble or if you think that the code could be improved, please open an issue of github.  
You can also contact me at hosvarshith@gmail.com