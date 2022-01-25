#! python3
# pypitopresults.py - opens several search results

import requests, sys, webbrowser, bs4

print('searching...')
res = requests.get(f'https://pypi.org/search/?q={sys.argv[1]}')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
link_elems = soup.select('.package-snippet')

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = f'https://pypi.org{link_elems[i].get("href")}'
    print(f'opening {url_to_open}')
    webbrowser.open(url_to_open)
