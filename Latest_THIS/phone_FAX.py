import phonenumbers

string='fax: 4444444444444'
def isPhoneNumber(text):
    for match in phonenumbers.PhoneNumberMatcher(text, None):
        print(match)
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdigit():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdigit():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdigit():
            return False
    return True

if string.find('fax:'or'Fax:'or 'F:'or 'f:'or 'fax'or'Fax'or 'F'or 'f'):
    print ('Success')