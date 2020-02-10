#The program should build a list of words.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    for word in line.split():
        if word in lst:
            continue;
        lst.append(word)

print(sorted(lst))
