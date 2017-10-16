#!pip3 install spacy
# coding=utf-8
from spacy.en import English

parser = English()

example = u'''
John and Jenny were accused of crimes by David
'''


def entities(example, show=False):
    if show: print(example)
    parsedEx = parser(example)

    print("-------------- entities only ---------------")
    # if you just want the entities and nothing else, you can do access the parsed examples "ents" property like this:
    ents = list(parsedEx.ents)
    tags = {}
    for entity in ents:
        # print(entity.label, entity.label_, ' '.join(t.orth_ for t in entity))
        term = ' '.join(t.orth_ for t in entity)
        if ' '.join(term) not in tags:
            tags[term] = [(entity.label, entity.label_)]
        else:
            tags[term].append((entity.label, entity.label_))
    print(tags)


entities(example)
