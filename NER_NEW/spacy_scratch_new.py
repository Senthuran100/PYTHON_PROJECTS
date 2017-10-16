import spacy
from spacy.pipeline import EntityRecognizer
from spacy.gold import GoldParse
from spacy.tagger import Tagger
import random

model_name = 'en'
entity_label = 'POS'
output_directory = 'D:/PYTHON/result/en_model'
train_data = [
    (u"Doctors don't have a normal working hour",
    [(0,len('Doctors'), 'POS')]),
    (u"Teachers teach there student",
    [(0,len('Teachers'), 'POS')]),
    (u"Civil Enginners works at site",
    [(0, len('Civil Enginners'), 'POS')]),
    (u"CEO is the top most position of the company",
    [(0,len('CEO'), 'POS')]),
    (u'Normal working hour of the Advocate is 8 hrs',
     [(len('Normal working hour of the '),len('Normal working hour of the Advocate'), 'POS')]),
    (u'He was a Software Engineer',
     [(len('He was a '),len('He was a Software Engineer'), 'POS')])
    # [(len('He was a Software '),len('He was a Software Engineer'),'L-ANIMAL')]

]
def train_ner(nlp, train_data, output_dir):
    # Add new words to vocab
    for raw_text, _ in train_data:
        doc = nlp.make_doc(raw_text)
        for word in doc:
            _ = nlp.vocab[word.orth]

    for itn in range(20):
        random.shuffle(train_data)
        for raw_text, entity_offsets in train_data:
            doc = nlp.make_doc(raw_text)
            gold = GoldParse(doc, entities=entity_offsets)
            nlp.tagger(doc)
            loss = nlp.entity.update(doc, gold)
    nlp.end_training()
    nlp.save_to_directory(output_dir)

nlp = spacy.load(model_name)
nlp.entity.add_label(entity_label)
ner = train_ner(nlp, train_data, output_directory)



