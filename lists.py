#Parse the From line and print out the second word in the line
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

for line in fh:
    line.rstrip()

    if not line.startswith("From:"):
        continue
    count += 1
    print(line.split()[1])

print("There were", count, "lines in the file with From as the first word")
