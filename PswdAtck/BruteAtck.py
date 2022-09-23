from zipfile import ZipFile
import string
import itertools


#Brute Force Attack
def zipCrack():
    zf = "Flag.brute.zip"
    encoding = "utf-8"
    max_password_length = 8
    chars = 0
    with ZipFile(zf) as f:
        while chars < max_password_length:
            print("Trying ", chars, "charcaters")
            for guess in itertools.product(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*+" + "",
                    repeat=chars):
                guess = ''.join(guess)
                try:
                    print(guess)
                    f.extractall(pwd=bytes(guess, encoding))
                    with open("Flag.txt") as d:
                        data = d.readlines()
                        print(data)
                        return True
                except:
                    pass
            chars += 1

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
