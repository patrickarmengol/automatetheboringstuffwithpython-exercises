import requests, os, bs4, threading



def xkcd_down(start_comic, end_comic):
    for comic_num in range(start_comic, end_comic + 1):
        comic_url = f'https://xkcd.com/{comic_num}'
        
        print(f'downloading page {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        img_elem = soup.select('#comic img')
        if img_elem == []:
            print('could not find comic image')
            continue
        image_url = f'https:{img_elem[0].get("src")}'
        
        print(f'downloading image {image_url}...')
        res = requests.get(image_url)
        res.raise_for_status()

        with open(os.path.join('chapter17/xkcd', os.path.basename(image_url)), 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)

def get_latest_xkcd_num():
    res = requests.get('http://xkcd.com')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    meta_url = soup.select('head > meta[property="og:url"]')[0].get('content')
    return int(meta_url[17:-1])


def main():
    latest = get_latest_xkcd_num()

    download_threads = []
    os.makedirs(input('input dir: '), exist_ok=True)

    for i in range(1, latest, 20):
        start = i
        end = min(i+19, latest)
        t = threading.Thread(target=xkcd_down, args=[start, end])
        download_threads.append(t)
        t.start()
    
    for dt in download_threads:
        dt.join()
    print('done')

if __name__ == '__main__':
    main()