#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    with open(files[i]) as f:
        shebang = f.read(22)

        if files[i][len(files[i]) - 3:] == ".py" and len(shebang) > 0:
            print(files[i])
        elif shebang == "#!/usr/bin/env python3":
            print(files[i])

    i += 1
