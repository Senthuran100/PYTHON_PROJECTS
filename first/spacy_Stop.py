from spacy import en
# en.STOP_WORDS.add('SRI LANKA')
# nlp = en.English()
# for word in en.STOP_WORDS:
#     lexeme = nlp.vocab[word]
#     lexeme.is_stop = True
# import  spacy
nlp = en.English()
lex = nlp.vocab[u'SRI LANKA']
lex.is_stop = False
doc = nlp(u'SRI LANKA is a country')
[(w.text,w.is_stop) for w in doc]
print(w.text)
print(w.is_stop)