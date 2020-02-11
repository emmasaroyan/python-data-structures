#The program reads through the file and figures out who has sent the greatest number of mail messages.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
max_count = None
max_word = None

for line in handle:
    line.rstrip()
    if not line.startswith("From:"):
        continue
    emails = line.split()[1]
    counts[emails] = counts.get(emails,0) + 1

for word, count in counts.items():
    if max_count is None or count > max_count:
        max_word = word
        max_count = count

print(max_word, max_count)
