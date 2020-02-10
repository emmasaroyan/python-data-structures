'''
    Count the lines of the form  X-DSPAM-Confidence:    0.8475
    and
    extract the floating point values from each of the lines
    and compute the average of those values
'''


# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    number = float(line[line.find("0."):len(line)+1])
    total += number


print ("Average spam confidence:",total/count)
