hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)
if h > 40.0:
    overtime = h - 40.0
    o = float(overtime)
    overtimePay = o * (r * 1.5)
    h = 40.0
else: 
    overtimePay = 0.0
pay = (h * r) + overtimePay
print pay