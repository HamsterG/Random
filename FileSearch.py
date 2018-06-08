import glob

textfiles = []
for file in glob.glob("*.txt"):
    textfiles.append(file)
print(textfiles)
