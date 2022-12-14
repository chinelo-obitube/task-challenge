import re

pattern = '/[a-zA-Z0-9]{3}$'
url_string = 'https://ionaapp.com/assignment-magic/dk/long/14t'
result = re.findall(pattern, url_string)

if result:
  print("Contains Alphanumeric.")
else:
  print("Does not contain Alphanumeric.")
