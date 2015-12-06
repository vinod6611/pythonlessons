inp = raw_input("What is the total hours?")
hours = float(inp)
inp = raw_input("How much is it pay per hour?")
rate = float(inp)
print rate, hours
if hours <=40:
    pay=rate*hours
else :
    pay=rate*40+(rate*1.5*(hours-40))
print pay
