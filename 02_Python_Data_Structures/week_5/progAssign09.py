name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)
counts = dict()

for line in fhandle:
    if not line.startswith("From: "): 
        continue
    else:
        words = line.split()
        counts[words[1]] = counts.get(words[1],0)+1

bigName = None
bigCount = None

for name, count in counts.items():
    if count is None or count > bigCount:
        bigName = name
        bigCount = count  

print bigName, bigCount





    

