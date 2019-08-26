import os

from shai import Shai
text = Shai.shai()

with open("/data/outputfiledocker.txt", "w") as f:
    f.write(text)
    print(text, text, text)