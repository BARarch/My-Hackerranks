regex_pattern = r"^M{,3}(CM)?(CD|D?)(XC|C{,3})(XL|L?)(IX|X{,3})(IV|V?)I{,3}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
