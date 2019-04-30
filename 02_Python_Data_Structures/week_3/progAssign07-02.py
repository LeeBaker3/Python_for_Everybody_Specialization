# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
	print ("Invalid filename")

count = 0
total = 0	
	
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(":")
    value = line[pos+1:len(line)]
    fValue = float(value)
    total = total + fValue

averageValue = str(total / count)

print "Average spam confidence: " + averageValue



