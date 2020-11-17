import re

x = re.match('^a...s$','alfias')
if x:
    print('Search successfull')
else:
    print('Not found')