# coding=utf-8
import spacy
nlp=nlp = spacy.load('en')
doc = nlp(u"""Masheesh Ikram 
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501, Galle Road, Colombo 06, SRI LANKA
Tel +94 (0) 11 2364 400. f +94 (0) 11 2364401. Mobile +94 (0) 779050954 
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linkoping.""")
for word in doc:
    # if(word.pos_=='NOUN'):
    print(word.text, word.lemma, word.lemma_, word.tag, word.tag_, word.pos, word.pos_)