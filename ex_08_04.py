fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
fh = open(fname)
lst = list()

for line in fh:
    x = line.rstrip()
    #lst.append(line)

    x = line.split()
    for word in x:
        if word not in lst:
            lst.append(word)
lst.sort()
    #.append()
print (lst)
