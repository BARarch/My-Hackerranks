import re
codePattern = re.compile(r'#([\dA-Fa-f]{6}|[\dA-Fa-f]{3})[^\w\d]')
valuePattern = re.compile(r':.*;')
