
from spacy.en import English
nlp = English()
# length=len('\n')
# print (length)
doc = nlp(u'The cat and the dog sleep in the basket near the door.')
for np in doc.noun_chunks:
    np.text
