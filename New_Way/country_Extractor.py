# coding=utf-8
from estnltk import Text

text = Text('''David Anderson			
Email: donato@example.com
Chief Executive Officer		        
Office 800-555-5555
Broadlook Technologies	                
Cell : 414-555-5555
21140 Capitol Drive		        
Fax   : 262-754-8081
Pewaukee WI 53072			
Blog www.idanato.com
http://www.broadlook.com
    ''')

# Extract named entities
print(text.named_entities)