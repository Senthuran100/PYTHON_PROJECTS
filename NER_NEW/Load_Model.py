# coding=utf-8
import spacy
nlp = spacy.load("en")
sample_text = """
Masheesh Ikram
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501, Galle Road, Colombo 06, SRI LANKA
Tel +94  011 2364 400. Fax +94  011 2364401. Mobile +94  0779050954 
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linkoping
"""
doc= nlp(unicode(sample_text))
for noun in doc.noun_chunks:
    print noun.text