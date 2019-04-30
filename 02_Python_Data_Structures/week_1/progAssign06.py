text = "X-DSPAM-Confidence:    0.8475"
l = len(text)
startpos = text.find("0")
n = text[startpos+1:l]
f = float(n)
print f