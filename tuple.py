''' The program reads through the file
and figures out the distribution by hour of the day for each of the messages.
Once it has accumulated the counts for each hour, prints out the counts, sorted by hour
'''


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


time = dict()

for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()

    hour = words[5].split(":")
    time[hour[0]] = time.get(hour[0],0) + 1

lst = []

for a,b in time.items():
    lst.append((a,b))

lst.sort()


for a,b in lst:
    print (a,b)
