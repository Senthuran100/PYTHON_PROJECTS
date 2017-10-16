# coding=utf-8
import en_core_web_sm
import re
import nltk
nlp = en_core_web_sm.load()
from nltk.corpus import stopwords
from geotext import GeoText
import phonenumbers
import pyap
stop = stopwords.words('english')
# stopwords = nltk.corpus.stopwords.words('english')
stop.append('No')
stop.append('Mobile')
string = """
Martin
Secretary | IFS Welfare
122/2 Arnolda Place, Colombo
Tel +94 11 236 4400 (ext. 1722). Fax +94 11 236 4401. Mobile +94 71 563 9556 
asanka.gallege@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linkoping.

"""
string2 =unicode(string, "utf-8")
doc1 = nlp(string2)
sentence = doc1.text
for ent in doc1.ents:
    if ent.label_ == 'PERSON':
        print ('Name')
        print (ent.text)
    # elif ent.label_ == 'GPE':
    #     print ('GPE')
    #     print (ent.text)
    elif ent.label_ == 'ORG':
        print ('ORG')
        print (ent.text)
def extract_phone_numbers(string):

    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def Extract_Fax(string):
    r = re.compile(r'')
    


def phonenum():
 print 'PHONE'
 for match in phonenumbers.PhoneNumberMatcher(string, None):
     print phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def extract_URL(string) :
    match1 = re.search(r'\(?\b(http://|www[.])[-A-Za-z0-9+&amp;@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&amp;@#/%=~_()|]', string)
    # print 'URL   :', match1.group(0)
    # url_link = match1.group(0)
    # return match1.group(0)
    if match1:
        return match1.group(0)
    else:
        return 'NO URL FOUND'

# def extract_address(string) :
#     r1 = re.compile(r'^\d+\s[A-z]+\s[A-z]+')
#     return r1.findall(string)
# def ie_preprocess(document):
#     document = ' '.join([i for i in document.split() if i not in stop])
#     sentences = nltk.sent_tokenize(document)
#     sentences = [nltk.word_tokenize(sent) for sent in sentences]
#     sentences = [nltk.pos_tag(sent) for sent in sentences]
#     return sentences

def extract_cities(document):
    places = GeoText(document)
    print 'Cities :',places.cities
    print 'Countries :',places.countries
    city = places.cities
    if places.cities:
        print('Address')
        r2 = re.compile(r'([(\d|-|/){1-5}]+[,|-|\s]+[A-zZ]+[Aa-zZ]+.*)')
        add = r2.findall(document)
        # print add
        for text in add:
         for text1 in places.cities:
            if text1 in text:
                print(text)
        # print (r2.findall(document))
    elif places.cities is None :
        addresses = pyap.parse(document, country='US')
        for address in addresses:
            # shows found address
            print(address)

    else:
        print('No Address Found')
# def extract_names(document):
#     names = []
#     org = []
#     gpe = []
#     sentences = ie_preprocess(document)
#     for tagged_sentence in sentences:
#         for chunk in nltk.ne_chunk(tagged_sentence):
#             if type(chunk) == nltk.tree.Tree:
#                 if chunk.label() == 'ORGANIZATION':
#                     org.append(' '.join([c1[0] for c1 in chunk]))
#                 if chunk.label() == 'GPE':
#                     gpe.append(' '.join([c2[0] for c2 in chunk]))

    # print "Names :", names
    # print "Organization :", org
    #  print "GPE :", gpe
# def extract_orgnisation(document) :
#     org = []
#     sentences = ie_preprocess(document)
#     for tagged_sentence in sentences:
#         for chunk in nltk.ne_chunk(tagged_sentence):
#             if type(chunk) == nltk.tree.Tree:
#                 if chunk.label() == 'ORGANIZATION':
#                     org.append(' '.join([cs[0] for cs in chunk]))
#     return org

if __name__ == '__main__':
    numbers = extract_phone_numbers(string)
    emails = extract_email_addresses(string)
    # extract_names(string)
    url = extract_URL(string)
    extract_cities(string)
    # address = extract_address(string)
    phonenum()
print "PHONE    :", numbers
print "URL  :",  url
print "Emails :", emails
# print "Address :",address
# print "Organization :",org