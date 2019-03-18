import requests
from bs4 import BeautifulSoup
import urllib3

# disable HTTPS warnings
urllib3.disable_warnings()

## Fixing the bug
## This is sample file for web crawler

def count_words(url, the_word):
    # photon_requests_session = requests.sessions.Session()
    # photon_requests_session.verify = "D:/euctr.cer"
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)
    print(words)
    return len(words)


def main():
    url = 'https://www.clinicaltrialsregister.eu/ctr-search/trial/2017-002323-25/DK'
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content)
    print soup
    # word = 'code'
    # count = count_words(url, word)
    # print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))


if __name__ == '__main__':
    main()