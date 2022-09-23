from zipfile import ZipFile

#dictionary attack
def zipCrack():
    zf = "Flag.zip"
    encoding = "utf-8"
    with ZipFile(zf) as f:
        with open("dictionary.txt") as d:
            for word in d.readlines():
                try:
                    word = word.rstrip() #Used to remove any hidden character
                    print(word)
                    f.extractall(pwd=bytes(word, encoding))
                    with open("Flag.txt") as b:
                        data = b.readlines()
                        print(data)
                        return True
                except:
                    pass

zipCrack()

#normal zipfile opener
#try:
#    with ZipFile(zf) as z:
#        z.extractall(pwd=bytes(password, encoding))
#        with open("Flag.easy.txt") as p:
#            data = p.readlines()
#            print(data)
#except RuntimeError as e:
#    print(e.message)