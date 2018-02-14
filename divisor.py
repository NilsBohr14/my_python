# find the divisor




num = int(raw_input("Print the number: "))
print "ok, thanks"
	

def create_range():
	global num
	print "This is total number: %r" %range(1, num+1)

def calculation():
	global num
	final_list = [ ]
	for element in range(1, num+1):
		if num % element == 0:
			final_list.append(element)
	print "\nfinal list\n"
	print final_list
	
	
	

	
	
#user_input()
create_range()
calculation()
	