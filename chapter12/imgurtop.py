# https://imgur.com/search/score/all?q_type=png&q_all=coffee

import requests, os, bs4

query_base = 'https://imgur.com/search/score/all?q_type=png&q_all='


def imgur_top(term, out, num):
    os.makedirs(out, exist_ok=True)

    search_res = requests.get(query_base + term)
    search_res.raise_for_status()

    search_soup = bs4.BeautifulSoup(search_res.text, 'lxml')
    thumb_elems = search_soup.select('.image-list-link')
    gal_links = [thumb_elems[i].get('href') for i in range(num)]
    for link in gal_links:
        gal_res = requests.get('https://imgur.com' + link)
        gal_res.raise_for_status()

        gal_soup = bs4.BeautifulSoup(gal_res.text, 'lxml')
        #print(gal_res.text)
        # idk how to wait on page fully loaded
        image_elem = gal_soup.select('meta[property="og:image"]')[0] # page returned by requests doesn't have the img tags, but still has link so w.e.
        image_link = image_elem.get('content').rstrip('?fb')
        print(image_link)
        image_res = requests.get(image_link)
        image_res.raise_for_status()
        with open(f'{out}/{os.path.basename(image_link)}', 'wb') as image_file:
            for chunk in image_res.iter_content(100000):
                image_file.write(chunk)
        

        


def main():
    user_term = input('search term: ')
    user_out = input('output dir: ')
    user_num = 5
    imgur_top(user_term, user_out, user_num)
    



if __name__ == '__main__':
    main()