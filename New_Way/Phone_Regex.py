# coding=utf-8
import re

string = """Masheesh Ikram 
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International,
800-555-5555
No 501, Galle Road, Colombo 06, SRI LANKA
Tel +94 (0) 11 2364 400. Fax +94 (0) 11 2364401. Mobile 800-555-5555
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linköping."""

def extract_phone_numbers(string):
    match1 = re.search(r'\d{3}-\d{3}-\d{4}$', string)
    if match1:
        return match1.group(0)
    else:
        return '--'

if __name__ == '__main__':
 numbers = extract_phone_numbers(string)
 print (numbers)

