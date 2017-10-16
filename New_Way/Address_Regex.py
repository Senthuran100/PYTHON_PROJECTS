# coding=utf-8
import re

string = """Masheesh Ikram 
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501, Galle Road, Colombo 06, SRI LANKA
Tel +94 (0) 11 2364 400. Fax +94 (0) 11 2364401. Mobile +94 (0) 779050954 
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linköping."""

def extract_phone_numbers(string):
    r = re.compile(r'/\s+(\d{2,5}\s+)(?![a|p]m\b)(([a-zA-Z|\s+]{1,5}){1,2})?([\s|\,|.]+)?(([a-zA-Z|\s+]{1,30}){1,4})(court|ct|street|st|drive|dr|lane|ln|road|rd|blvd)([\s|\,|.|\;]+)?(([a-zA-Z|\s+]{1,30}){1,2})([\s|\,|.]+)?\b(AK|AL|AR|AZ|CA|CO|CT|DC|DE|FL|GA|GU|HI|IA|ID|IL|IN|KS|KY|LA|MA|MD|ME|MI|MN|MO|MS|MT|NC|ND|NE|NH|NJ|NM|NV|NY|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VA|VI|VT|WA|WI|WV|WY)([\s|\,|.]+)?(\s+\d{5})?([\s|\,|.]+)/i')
    phone_numbers = r.findall(string)
    print (phone_numbers)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

if __name__ == '__main__':
 numbers = extract_phone_numbers(string)
 print (numbers)
