from geotext import GeoText
import re
string = """
Masheesh Ikram 
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501,  Galle Road  Colombo 06, SRI LANKA
Tel +94 (0) 11 2364 400. Fax +94 (0) 11 2364401. Mobile +94 (0) 779050954 
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linkoping.
"""
def extract_cities(document):
    places = GeoText(document)
    print 'Cities :',places.cities
    print 'Countries :',places.countries
    city = places.cities
    if places.cities:
        print('Address')
        r2 = re.compile(r'([\d{1-4}]+[,|-|\s]+[A-zZ]+[Aa-zZ]+.*)')
        add = r2.findall(document)
        for text in add:
            if 'Colombo' in text:
                print(text)

    else:
        print('No Address')

if __name__ == '__main__':
    extract_cities(string)