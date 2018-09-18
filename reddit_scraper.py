#python3

import urllib.request
from bs4 import BeautifulSoup

url = "https://www.reddit.com/top/"

# download url and extract contents to variable html
# using unique User-Agent in headers in accordance with 
# reddit.com documentation
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla:redditbot:v0.1 + (by /u/thejcode24)'})
html = urllib.request.urlopen(request).read()

# pass html to Beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

# get html of the main table which holds the entire reddit page 
# table within div with id='siteTable'
main_table = soup.find("div", attrs={'id':'siteTable'})

# within div id=siteTable, find all elements class="title"
links = main_table.find_all("a",class_="title")

# from each links element found, get text of link and url link 
# store in a list as dictionary format
list_links = []

for link in links:
    title = links.text
    url = link['href']
    record = {
        'title':title,
        'url':url
    }

    list_links.append(record)

print(list_links)