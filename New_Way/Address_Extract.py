# coding=utf-8
from nltk import Text

text = Text('''Eesti Vabariik on riik Põhja-Euroopas.
    Eesti piirneb põhjas üle Soome lahe Soome Vabariigiga.
    Riigikogu on Eesti Vabariigi parlament. Riigikogule kuulub Eestis seadusandlik võim.
    2005. aastal sai peaministriks Andrus Ansip, kes püsis sellel kohal 2014. aastani.
    2006. aastal valiti presidendiks Toomas Hendrik Ilves.
    ''')

# Extract named entities
print(text.named_entities)
