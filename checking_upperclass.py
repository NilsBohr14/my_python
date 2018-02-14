s = "A B c d e F G h I"
spl = s.split(" ")
print spl
upper = 0
lower = 0
upper_list = []
lower_list = []
for c in s:
 
    if c.isupper() == True:
        upper_list.append(c)
    if c.islower() == True:
        lower_list.append(c)
        
print upper_list
for item in upper_list:
    upper += 1
print upper 

print lower_list
for item in lower_list:
    lower+=1
#print ull
print lower