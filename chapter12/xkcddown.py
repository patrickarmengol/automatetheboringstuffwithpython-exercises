#! python3
# xkcddown.py - download all xkcd comics

import requests, os, bs4

url = 'https://xkcd.com'
out_dir = 'chapter12/xkcd'
os.makedirs(out_dir, exist_ok=True)

print('starting...')

while not url.endswith('#'):
    page_res = requests.get(url)
    page_res.raise_for_status()
    
    soup = bs4.BeautifulSoup(page_res.text, 'lxml')
    try:
        image_elem = soup.select('#comic img')[0]
    except IndexError:
        prev_elem = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_elem.get('href')
        continue
    image_link = 'https:' + image_elem.get('src')
    image_title = image_elem.get('alt')
    image_name = os.path.basename(image_link) # take filename directly 
    
    print(f'downloading: {image_title}')

    image_res = requests.get(image_link)
    image_res.raise_for_status()

    print(f'writing into: {image_name}')

    with open(f'{out_dir}/{image_name}', 'wb') as image_file:
        for chunk in image_res.iter_content(100000):
            image_file.write(chunk)
    
    prev_elem = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_elem.get('href')

print('done')