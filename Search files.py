import os

filePaths = []

counter = 0
inp = input("What file shall we search for mi'lord:  ")
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
