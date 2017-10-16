import nltk

File = open("D:\IFS\input\source.txt")  # open file
lines = File.read()

# my_sent = """JOHN JONES
#             MARKETING DEPARTMENT
# 10-123 1/2 MAIN STREET NW
# MONTREAL QC  H3Z 2Y7
# Canada"""

parse_tree = nltk.ne_chunk(nltk.tag.pos_tag(lines.split()), binary=True)  # POS tagging before chunking!

named_entities = []

for t in parse_tree.subtrees():
    if t.label() == 'NE':


        # named_entities.append(t)
         named_entities.append(list(t))  # if you want to save a list of tagged words instead of a tree

print named_entities

from geotext import GeoText
places = GeoText(lines)
print "Locations :", places.cities


import re
# line = "senthuran.manoharan@gmail.com"
match = re.search(r'[\w\.-]+@[\w\.-]+', lines)
print 'Email :',  match.group(0)
# print match.group(0)

match1 = re.search(r'\(?\b(http://|www[.])[-A-Za-z0-9+&amp;@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&amp;@#/%=~_()|]', lines)
print 'URL   :', match1.group(0)


