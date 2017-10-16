# coding=utf-8
import nltk
import textblob

f = open('D:\IFS\input\person.txt')
csv_f = f.readlines()


# dataset = []
#
# for row in csv_f:
#       dataset.append(({'Position': row[0]}, row[1]))
#
# print (dataset)

classifier = nltk.NaiveBayesClassifier.train(csv_f)

mydata ="""
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
print (mydata, classifier.classify(mydata))
