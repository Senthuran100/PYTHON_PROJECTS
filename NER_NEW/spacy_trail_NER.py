import spacy
nlp = spacy.load('en')
doc = nlp(u'London is a big city in the United Kingdom.')
for ent in doc.ents:
    print(ent.label_, ent.text)