import spacy
import random
from spacy.gold import GoldParse
from spacy.language import EntityRecognizer

train_data = [
    ('Who is Chaka Khan?', [(7, 17, 'PERSON')]),
    ('I like London and Berlin.', [(7, 13, 'LOC'), (18, 24, 'LOC')])
]

nlp = spacy.load('en', entity=False, parser=False)
ner = EntityRecognizer(nlp.vocab, entity_types=['PERSON', 'LOC'])

for itn in range(5):
    random.shuffle(train_data)
    for raw_text, entity_offsets in train_data:
        doc = nlp.make_doc(raw_text)
        gold = GoldParse(doc, entities=entity_offsets)

        nlp.tagger(doc)
        ner.update(doc, gold)
ner.model.end_training()