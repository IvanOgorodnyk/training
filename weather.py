import random
passlen = int(input("enter the leght of password:"))
s="qwertzuiopasdfghjklyxcvbnm1234567890QWERTZUIOPASDFGHJKLYXCVBNM!§$%&/()=?"
p = "".join(random.sample(s,passlen ))
print (p)
