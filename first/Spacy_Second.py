# coding=utf-8
import spacy
from spacy.en import English
import en_core_web_sm

nlp = en_core_web_sm.load()
doc1 = nlp(u"""David Anderson	Email: donato@example.com
Chief Executive Officer		        Office 800-555-5555
Broadlook Technologies	                Cell : 414-555-5555
21140 Capitol Drive		        Fax   : 262-754-8081
Pewaukee WI 53072			Blog www.idanato.com
http://www.broadlook.com
""")
sentence = doc1.text
for ent in doc1.ents:
    if ent.label_ == 'PERSON':
            print ('Names', ent.text)
    elif ent.label_ == 'GPE':
            print ('GPE')
            print (ent.text)
    elif ent.label_ == 'ORG':
            print ('ORG')
            print (ent.text)
    elif ent.label_ == 'CARDINAL':
            print ('Cardinal')
            print (ent.text)
    elif ent.label_ == 'FACILITY':
            print ('Facility')
            print (ent.text)
    # elif ent.label == 'ORG':
    #     sentence = sentence[:ent.start_char] + sentence[ent.start_char:].replace(ent.text, '<' + ent.text + '>', 1)

    # print(sentence[:ent.start_char] + sentence[ent.start_char:])
