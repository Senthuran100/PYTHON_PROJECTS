import requests
from bs4 import BeautifulSoup


def get_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "xml")

    # delete unwanted tags:
    for s in soup(['figure', 'script']):
        s.decompose()

    article_soup = [s.get_text() for s in soup.find_all(
        'div', {'class': 'story-body__inner'})]

    text = ''.join(article_soup)
    return text


# Human Names tokenization using nltk
import nltk
from nameparser.parser import HumanName


def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary=False)
    names = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1:  # ignore surnames only
            for part in person:
                name += part + ' '
            if name[:-1] not in names:
                names.append(name[:-1])
            name = ''
        person = []
    print(names)
    first_names = []
    for name in names:
        first_name = HumanName(name).first
        first_names.append(first_name)
    return first_names


def main():
    url = "http://www.bbc.co.uk/news/uk-politics-39634650"  # works kind of fine...
    # url = "http://www.bbc.co.uk/news/uk-politics-39633696" #doesn't pick up Theresa May
    # url = "http://www.bbc.co.uk/news/uk-politics-39636471" #UnicodeEncodeError: 'ascii' codec can't encode character
    text = get_text(url)
    print(text)
    first_names = get_human_names(text)
    print(first_names)


if __name__ == '__main__':
    main()
