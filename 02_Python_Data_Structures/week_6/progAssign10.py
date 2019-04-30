name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)
counts = dict()

for line in fhandle:
    if not line.startswith("From"): 
        continue
    else:
        words = line.split()
        if len(words) >= 5:
            time = words[5].split(":")
            counts[time[0]] = counts.get(time[0],0)+1

for k, v in sorted(counts.items()):
    print k, v




    

