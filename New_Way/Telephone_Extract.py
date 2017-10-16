import phonenumbers
import os
import re
import sys

# fp =open("D:\IFS\input\source.txt","r")
fp="""
Masheesh Ikram
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501, Galle Road, Colombo 06, SRI LANKA
Tel +94 011 2364 400. Fax +94 (0) 11 2364401. Mobile +94 (0) 77905 0954 
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linkoping, Sweden.
"""
for i in phonenumbers.PhoneNumberMatcher(fp, None):
        if i is not None:
                print(i)
        else:
                print('TEL')
