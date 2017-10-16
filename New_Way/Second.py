from nltk import word_tokenize, pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk

sentence = "Mark and John are working at Google."
ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
iob_tagged = tree2conlltags(ne_tree)
# """
# [('Mark', 'NNP', u'B-PERSON'), ('and', 'CC', u'O'), ('John', 'NNP', u'B-PERSON'), ('are', 'VBP', u'O'), ('working', 'VBG', u'O'), ('at', 'IN', u'O'), ('Google', 'NNP', u'B-ORGANIZATION'), ('.', '.', u'O')]
# """
ne_tree = conlltags2tree(iob_tagged)
print(ne_tree)

# """
# (S
#   (PERSON Mark/NNP)
#   and/CC
#   (PERSON John/NNP)
#   are/VBP
#   working/VBG
#   at/IN
#   (ORGANIZATION Google/NNP)
#   ./.)
# """