# !usr/bin/env python
# coding=utf-8
# import phonenumbers
# import os
# import re
# import sys
#
# file_name = 'D:\IFS\input\source.txt'
# fp =open(file_name,"r")
# print (fp)
# fpp ="""
# David Anderson				        Email: donato@example.com
# Chief Executive Officer		        Office :+94 075 5647 945
# Broadlook Technologies	            Cell  : +91 9871127622
# 21140 Capitol Drive		            Fax   :+78 57880080888
# Pewaukee WI 53072			        Blog www.idanato.com
# http://www.broadlook.com
# """
#
# for line in fp:
#     for match in phonenumbers.PhoneNumberMatcher(line,None):
#         print match


import phonenumbers
import os
import re
import sys
import re

file_name = 'D:\IFS\input\source.txt'
fp =open(file_name,"r")

fpp="""
Masheesh Ikram
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501, Galle Road, Colombo 06, SRI LANKA
Tel +94 (0) 11 2364 400. Fax +94 (0) 11 2364401. Mobile +94 (0) 779050954 
masheesh.ikram@ifsworld.com | www.IFSWORLD.com 
IFS World Operations AB is a limited liability company registered in Sweden. 
Corporate identity number: 556040-6042. 
Registered office: Teknikringen 5, Box 1545, SE-581 15 Linkoping.
"""
print (len("""Masheesh Ikram
LEAD SOFTWARE ENGINEER 
Supply Chain | Research & Development
IFS R&D International, 
No 501, Galle Road, Colombo 06, SRI LANKA
Tel """))
y = '+94 (0) 11 2364 400'
# for line in fpp:
for match in phonenumbers.PhoneNumberMatcher(fpp,None):
        # print match
        tel =[]
        tel.append(match.raw_string)
        print (tel)
        match1 = re.search(r'(\w+)',fpp)
        if match1:
         print match1.group(0)



 # phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
