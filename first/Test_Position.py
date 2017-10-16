import nltk
import csv

f = open('D:\IFS\python_train\Position1.csv')
csv_f = csv.reader(f)
csv_f.next()  # skip the header line

dataset = []

for row in csv_f:
      dataset.append(({'Position': row[0]}, row[1]))

print (dataset)

classifier = nltk.NaiveBayesClassifier.train(dataset)

mydata = {'Position': 'Srilanka'}
print (mydata, classifier.classify(mydata))
