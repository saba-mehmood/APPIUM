import re
s = "This must not b3 delet3d, but the number at the end yes 1"
s = re.sub(" \d+", " ", s)
print(s)