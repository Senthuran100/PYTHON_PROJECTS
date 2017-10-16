import pyap
test_address = """
Valerie Richardson 
2906 N. Glenwood Terrace, Atlanta, GA 30310
(404) 555-0789
Valerie.Richardson@yahoo.com
    """
addresses = pyap.parse(test_address, country='US')
for address in addresses:
    # shows found address
     print(address)
    # shows address parts
    #  print(address.as_dict())