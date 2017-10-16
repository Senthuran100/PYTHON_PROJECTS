import nltk
import csv

f = open('D:\IFS\python_train\exp.csv')
csv_f = csv.reader(f)
csv_f.next()  #skip the header line

dataset = []

for row in csv_f:
      dataset.append(({'size': row[0], 'color': row[1], 'shape': row[2]}, row[3]))

print (dataset)

classifier = nltk.NaiveBayesClassifier.train(dataset)

mydata = {'size':'large', 'color':'purple', 'shape':' '}
print (mydata, classifier.classify(mydata))