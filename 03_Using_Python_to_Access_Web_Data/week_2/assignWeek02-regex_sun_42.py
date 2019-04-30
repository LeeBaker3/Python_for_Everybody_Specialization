import re
fname = "regex_sum_42.txt"
fhandle = open(fname)
total = 0
for line in fhandle:
    num = re.findall('[0-9]+',line)
    print num
    if len(num) == 0:
        continue
    else:
        total = total + sum(int(i) for i in num)
        print total
