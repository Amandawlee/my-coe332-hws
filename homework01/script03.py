def length(x):
    l = len(x) - 1
    return l

import names

fullname = []
for x in range(5):
    fullname.append(names.get_full_name())

for y in range(5):
    print(fullname[y])
    print(length(fullname[y]))

