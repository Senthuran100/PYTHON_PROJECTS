import pyap
test_address = """
    Lorem ipsum
    225 E. John Carpenter Freeway,
    Suite 1500 Irving, Texas 75062
    Dorem sit amet
    """
addresses = pyap.parse(test_address, country='US')
for address in addresses:
        # shows found address
        print(address)
        # shows address parts
        print(address.as_dict())