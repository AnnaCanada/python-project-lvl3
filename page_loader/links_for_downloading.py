from urllib.parse import urlparse


DICTIONARY = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def get_links_for_download(soup, url):
    list_of_links = []
    for key in DICTIONARY.keys():
        find_all = soup.find_all(key)
        atr = DICTIONARY.get(key)
        for link_to_download in find_all:
            file_link = link_to_download.get(atr)
            if is_same_domain(url, file_link):
                list_of_links.append((file_link, link_to_download, atr))
            else:
                continue
    return list_of_links


def is_same_domain(url, link):
    if not link:
        return False
    link_netloc = urlparse(link).netloc
    url_netloc = urlparse(url).netloc
    if link_netloc == url_netloc or not link_netloc:
        return True
    else:
        return False
