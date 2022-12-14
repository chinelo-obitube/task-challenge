import re

pattern = '/[a-zA-Z0-9]{2}$'
url_string = 'https://ionaapp.com/assignment-magic/dk/short/14'
result = re.findall(pattern, url_string)

if result:
  print("Contains Alphanumeric.")
else:
  print("Does not contain Alphanumeric.")
