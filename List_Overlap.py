# list over lap


#a = [1, 3, 3, 5, 5, 6, 7]
#b = [1, 3, 8, 9]

a = [ ]
b = [ ]
def list_a():
	global a
	a_len = int(raw_input("Please input the length: "))
	while len(a)<a_len:
		user_element = int(raw_input("Please enter the number you wanted to add list: "))
		a.append(user_element)
	print a
	

def list_b():
	global b
	b_len = int(raw_input("Please input the length: "))
	while len(b)<b_len:
		user_element = int(raw_input("Please enter the number you wanted to add list: "))
		b.append(user_element)
	print b
	


def merge():
	global a,b
	print "here is a:  ", a
	print "Here is b: ", b
	merged = a + b

	#print "Here is merged: ", merged
	s = set(merged)

	final_list = list(s)

	print "Here is desired final list: ", final_list

list_a()
list_b()
merge()




 