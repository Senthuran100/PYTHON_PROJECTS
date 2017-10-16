# coding=utf-8
from __future__ import unicode_literals, print_function
import json
import pathlib
import random

import spacy
from spacy.pipeline import EntityRecognizer
from spacy.gold import GoldParse
from spacy.tagger import Tagger
from itertools import groupby
import unicodedata

import sys

try:
    unicode
except:
    unicode = str


def train_ner(nlp, train_data, entity_types):
    # Add new words to vocab.
    for raw_text, _ in train_data:
        doc = nlp.make_doc(raw_text)
        for word in doc:
            _ = nlp.vocab[word.orth]

    # Train NER.
    ner = EntityRecognizer(nlp.vocab, entity_types=entity_types)
    for itn in range(5):
        random.shuffle(train_data)
        for raw_text, entity_offsets in train_data:
            doc = nlp.make_doc(raw_text)
            gold = GoldParse(doc, entities=entity_offsets)
            ner.update(doc, gold)
    return ner


def save_model(ner, model_dir):
    model_dir = pathlib.Path(model_dir)
    if not model_dir.exists():
        model_dir.mkdir()
    assert model_dir.is_dir()

    with (model_dir / 'config.json').open('wb') as file_:
        data = json.dumps(ner.cfg)
        if isinstance(data, unicode):
            data = data.encode('utf8')
        file_.write(data)
    ner.model.dump(str(model_dir / 'model'))
    if not (model_dir / 'vocab').exists():
        (model_dir / 'vocab').mkdir()
    ner.vocab.dump(str(model_dir / 'vocab' / 'lexemes.bin'))
    with (model_dir / 'vocab' / 'strings.json').open('w', encoding='utf8') as file_:
        ner.vocab.strings.dump(file_)


def main(model_dir=None):
    nlp = spacy.load('en', parser=False, entity=False, add_vectors=False)

    # v1.1.2 onwards
    if nlp.tagger is None:
        print('---- WARNING ----')
        print('Data directory not found')
        print('please run: `python -m spacy.en.download --force all` for better performance')
        print('Using feature templates for tagging')
        print('-----------------')
        nlp.tagger = Tagger(nlp.vocab, features=Tagger.feature_templates)

    train_data = [
        ("Masheesh Ikram\nLEAD SOFTWARE ENGINEER\nSupply Chain | Research & Development\nIFS R&D International, \nNo 501, Galle Road, Colombo 06, SRI LANKA\nTel +94 (0) 11 2364 400. Fax +94 (0) 11 2364401. Mobile +94 (0) 779050954\nmasheesh.ikram@ifsworld.com | www.IFSWORLD.com \nIFS World Operations AB is a limited liability company registered in Sweden. \nCorporate identity number: 556040-6042. \nRegistered office: Teknikringen 5, Box 1545, SE-581 15 Linköping.",
         [(len('Masheesh Ikram\n'), len('Masheesh Ikram\nLEAD SOFTWARE ENGINEER'), 'POS')]),
        ("Asanka Gallege\nSecretary | IFS Welfare\n501, Galle Road, Colombo 06,   SRI LANKA\nTel +94 11 236 4400 (ext. 1722). Fax +94 11 236 4401. Mobile +94 71 563 9556\nasanka.gallege@ifsworld.com | www.IFSWORLD.com \nIFS World Operations AB is a limited liability company registered in Sweden. \nCorporate identity number: 556040-6042. \nRegistered office: Teknikringen 5, Box 1545, SE-581 15 Linköping.",
         [(len('Asanka Gallege\n'), len('Asanka Gallege\nSecretary'), 'POS')]),
        ("David Anderson\nEmail: donato@example.com\nChief Executive Officer\nOffice  800-555-5555 \nBroadlook Technologies	\nCell :  414-555-5555 \n21140 Capitol Drive\nFax   : 262-754-8081\nPewaukee WI 53072\nBlog www.idanato.com\nhttp://www.broadlook.com",
         [(len('David Anderson\nEmail: donato@example.com\n'), len('David Anderson\nEmail: donato@example.com\nChief Executive Officer'), 'POS')]),
        ("Valerie Richardson \nAccountant\n2906 N. Glenwood Terrace, Atlanta, GA 30310\n(404) 555-0789\nValerie.Richardson@yahoo.com\n501, Galle Road, , Colombo 06,  SRI LANKA\nTel +94 11 236 44 00. Fax +94 11 236 44 01\nchathuri.gamage@ifsworld.com | www.IFSWORLD.com ",
         [(len('Valerie Richardson \n'), len('Valerie Richardson \nAccountant'), 'POS')]),
        ('Kandasamy Yogendirakumar (Yogi)\nMSc, MBCS, MIET | DIRECTOR IFS ACADEMY \n501, Galle Road, Colombo 06,   SRI LANKA\nTel +94 (0)112 364 440. Fax +94 (0)112 364 441. Mobile +94 (0)714 039 089 \nkandasamy.yogendirakumar@ifsworld.com|www.IFSWORLD.com \nIFS World Operations AB is a limited liability company registered in Sweden. \nCorporate identity number: 556040-6042. \nRegistered office: Teknikringen 5, Box 1545, SE-581 15 Linköping.',
         [(len('Kandasamy Yogendirakumar (Yogi)\nMSc, MBCS, MIET | '), len('Kandasamy Yogendirakumar (Yogi)\nMSc, MBCS, MIET | DIRECTOR'), 'POS')]),
        ('He was a  Software Engineer.',
         [(len('He was a '), len('He was a Lead Software Engineer'),'POS')]),
        ('I am an Engineer',
         [(len('I am an '), len('I am an Engineer'), 'POS')]),
        ('I am an Lead Engineer as well as Software Engineer in IFS.',
         [(len('I am an '), len('I am an Lead Engineer'), 'POS'),(len('I am an Lead Engineer as well as '), len('I am an Lead Engineer as well as Software Engineer'), 'POS')]),
        ('Secretary',
         [(0, len('Secretary'), 'POS')]),
        ('Chief Executive Officer',
         [(0, len('Chief Executive Officer'), 'POS')]),
        ('David Anderson Secretary',
         [(len('David Anderson'),len('David Anderson Secretary'), 'POS')]),
        ('David Anderson\nSecretary',
         [(len('David Anderson\n'), len('David Anderson Secretary'), 'POS')]),
        ('Asanka Gallege\nSecretary | IFS Welfare\n501, Galle Road, Colombo 06, SRI LANKA\nTel +94 11 236 4400 (ext. 1722). Fax +94 11 236 4401. Mobile +94 71 563 9556',
         [(len('Asanka Gallege\n'), len('Asanka Gallege\nSecretary'), 'POS')]),
        ('Fredrik Vom\nGROUP SENIOR VICE PRESIDENT\nBusiness Development\nGullbergs Strandgata 15, SE-411 04 Goteborg,SWEDEN\nTel +46 31 726 3046. Fax +46 31726 3001. Mobile +46 733 453046\nfredrik.vom.hofe@ifsworld.com | www.IFSWORLD.com\nIFS World Operations AB is a limited liability company registered in Sweden.',
        [(len('Fredrik Vom\n'), len('Fredrik Vom\nGROUP SENIOR VICE PRESIDENT'), 'POS')]),
        (
        'Fredrik Vom\nGROUP SENIOR VICE PRESIDENT\nBusiness Development\nGullbergs Strandgata 15, SE-411 04 Goteborg,SWEDEN\nTel +46 31 726 3046. Fax +46 31726 3001. Mobile +46 733 453046\nfredrik.vom.hofe@ifsworld.com | www.IFSWORLD.com\nIFS World Operations AB is a limited liability company registered in Sweden.',
        [(len('Fredrik Vom\n'), len('Fredrik Vom\nGROUP SENIOR VICE PRESIDENT'), 'POS')]),
        (
         'Dr. Ashok Padhye\nGeneral Physician\nA-205, Natasha Apartments\n2, Inner Ring Road\nDomlur\nBANGALORE - 560071\nKarnataka',
            [(len('Dr. Ashok Padhye\n'), len('Dr. Ashok Padhye\nGeneral Physician'), 'POS')]),
        (
            'Dr. Ashok Padhye\nGeneral Physician\nA-205, Natasha Apartments\n2, Inner Ring Road\nDomlur\nBANGALORE - 560071\nKarnataka',
            [(len('Dr. Ashok Padhye\n'), len('Dr. Ashok Padhye\nGeneral Physician'), 'POS')]),

    ]
    # file_name = 'D:\PYTHON\Input\input.txt'
    # train_data = open(file_name, "r")
    ner = train_ner(nlp, train_data, ['POS'])

    doc = nlp.make_doc("""  
I am an Lead Engineer as well as Software Engineer in IFS.
""")
    doc1 = unicode(doc)
    nlp.tagger(doc)
    ner(doc)

    position=[]
    for word in doc:
        if word.ent_type_ == 'POS':
            position.append(word.text)
            # print(word.text,word.ent_type_, word.ent_iob)
    # print(position)
    # position=[word for word in doc if word.ent_type =='POS']
    # print (position)
    i =0
    pos =[]
    new_pos =[]
    pos=position
    for x in pos:
        if word.ent_iob ==3 and i!=0:
            new_pos.append(pos[:i])
            pos=position[i:]
        elif i==len(position)-1:
            new_pos.append(pos)

        i+=1
    for y in new_pos:
        string=" ".join(str(x) for x in y)
        print(string)
    # print (doc1)


    if model_dir is not None:
        save_model(ner, model_dir)

if __name__ == '__main__':
    main('ner')
