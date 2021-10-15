import requests
from bs4 import BeautifulSoup

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

class Translate():
    def __init__(self, word) -> None:
        self.word = word
        self.word_vi = ""
    
    def translate_word(self):
        word_en = self.word.split(' ')[0].lower()
        url = 'https://dictionary.cambridge.org/vi/dictionary/english-vietnamese/{}'.format(word_en)
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.text, "lxml")
        word_vi = soup.find_all('span', {'class': 'trans dtrans'})
        if word_vi:
            self.word_vi = word_vi[0].text
        return self.word_vi
